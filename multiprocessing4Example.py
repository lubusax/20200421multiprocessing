"""
Process class can also be subclassed just like threading.Thread;
Queue works like queue.Queue but for cross-process, not cross-thread
"""

import os, time, queue
import multiprocessing as mp
from multiprocessing import Process, Queue

# process-safe shared queue
# queue is a pipe + locks/semafores

class Counter(Process):
  label = ' @'
  def __init__(self, start, queue):
    self.state = start    # retain state for use in run
    self.post = queue
    Process.__init__(self)

  def run(self):      # run in new process on start()
    for i in range(3):
      time.sleep(1)
      self.state += 1
      print(            # self.pid is this child's pid
        self.label ,self.pid, self.state) 
      self.post.put(    # stdout file is shared by all
        [self.pid, self.state])
    print(self.label, self.pid, '-')
    os._exit(120)

def anyProcessAlive(Processes):
  allDead = True
  for i in range(len(Processes)):
    if Processes[i].is_alive():
      allDead = False
      break
  anyoneAlive = not allDead
  return anyoneAlive
  
if __name__ == '__main__':
  print('start', os.getpid())
  print('number of CPUs: ', mp.cpu_count())
  print('number of usable CPUs: ',len(os.sched_getaffinity(0)))
  print('list of all supported start methods: ',mp.get_all_start_methods())
  print('name of start method used for starting processes: ', mp.get_start_method())

  post = Queue()
  p = Counter(0, post)    # start 3 processes sharing queue
  q = Counter(100, post)  # children are producers
  r = Counter(1000, post)

  p.start(); q.start(); r.start()

  processList = mp.active_children()

  while anyProcessAlive(processList):         # parent consumes data on queue
    time.sleep(0.5)       # this is essentially like a GUI,
    try:                  # though GUIs often use threads
      data = post.get(block=False)
    except queue.Empty:
      print('no data...')
    else:
      print('posted:', data)

  p.join(); q.join(); r.join()  # must get before join putter
  print('finished pid %s with exitcode %s' % (os.getpid(), r.exitcode)) # exitcode is child exit status
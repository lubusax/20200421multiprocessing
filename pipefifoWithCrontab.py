import os, time, sys

fifoname = '/tmp/pipefifo'
fileCrontab = '/home/pi/crontabTask'
taskDir = '/home/pi/Documents/2004_terminal/'
taskFileName = 'simpleTask.py'

def loopReadPipe():
  pipein = open(fifoname, 'r')
  # open fifo as text file object
  while True:
    line = pipein.readline()[:-1]
    if line:
      print('this pipe end %d got "%s" ' % (
        os.getpid(), line))

def createCrontabfile():
  file = open(fileCrontab, 'w')
  line = '* * * * * python3 ' + taskDir + taskFileName + '\n'
  file.write(line)
  file.close()

def setupCrontab():
  createCrontabfile()
  os.system(
    'crontab -u pi ' + fileCrontab)


if __name__ == '__main__':

  if not os.path.exists(fifoname):
    os.mkfifo(fifoname)
  
  if not os.path.exists(fileCrontab):
    setupCrontab()
  
  loopReadPipe()

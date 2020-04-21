"Use multiprocessing to start independent programs, os.fork or not"
import os
import sys
from multiprocessing import Process

def runprogram(arg):
  os.execlp('python3', 'python3', 'child.py', str(arg))

if __name__ == '__main__':
  print('python version: ', sys.version)
  for i in range(5):
    Process(target=runprogram, args=(i*i,)).start()
  print('parent exit')
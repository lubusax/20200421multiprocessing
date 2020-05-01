import os, time, sys

fifoname = '/tmp/pipefifo'
fileCrontab = '/home/pi/crontabTask'
taskDir = '/home/pi/Documents/2004_cpp_rpi/wiringPiExamples/'
taskFileName = 'test3Display'

def createCrontabfile():
  file = open(fileCrontab, 'w')
  line = '* * * * * ' + taskDir + taskFileName + '\n'
  file.write(line)
  file.close()

def setupCrontab():
  createCrontabfile()
  os.system(
    'crontab -u pi ' + fileCrontab)


if __name__ == '__main__':
  
  #if not os.path.exists(fileCrontab):
  setupCrontab()
  

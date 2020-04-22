import os, time
from time import gmtime, strftime

timeDisplay = strftime(
  "%a, %d %b %Y %H:%M:%S +0000", gmtime())
fifoname = '/tmp/pipefifo'

pipeout = os.open(fifoname, os.O_WRONLY)

msg = (timeDisplay).encode()  # binary
os.write(pipeout, msg)
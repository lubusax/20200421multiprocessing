import os, sys

#print('python version (child.py): ', sys.version)

print('Hello from child with pid: %s' % (os.getpid() ))
#l = str(sys.argv)
for i in range(len(sys.argv)):
  print('arg %s: %s' % (
    i, sys.argv[i]))
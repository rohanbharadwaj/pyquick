#!/usr/bin/python -tt
import sys
import os
import commands

def List(dir):
  cmd='ls -l ' + dir
  print 'about to do this:', cmd
  (status,output) = commands.getstatusoutput(cmd)
  if status:
    print sys.stderr.write('there was an error:'+ output)
    sys.exit(1)
  print output

def main():
  List(sys.argv[1])

if __name__=='__main__':
  main() 

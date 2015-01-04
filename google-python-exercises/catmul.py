#!/usr/bin/python -tt
import sys

def cat(filename):
  try:
    f = open(filename, 'rU') #U ignare dos line ending unix
    print '-----',filename
    text = f.read() #having just 1 string
    print text
    f.close()
  except IOError:
    print 'No File',filename 
def main():
  args = sys.argv[1:]
  for arg in args:
    cat(arg)

if __name__ == '__main__':
  main()


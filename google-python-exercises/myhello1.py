import sys

def cat(filename):
  f = open(filename, 'rU') #U ignare dos line ending unix
  #lines = f.readlines()
  #print lines
  text = f.read() #having just 1 string
  print text
  f.close()
def main():
  cat(sys.argv[1])

if __name__ == '__main__':
  main()


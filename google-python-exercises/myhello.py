import sys

def cat(filename):
  f = open(filename, 'rU') #U ignare dos line ending unix
  for line in f:
    print line,  # inhabits trailing newline
  f.close()
def main():
  cat(sys.argv[1])

if __name__ == '__main__':
  main()


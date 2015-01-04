#!/usr/bin/python

# import modules used here -- sys is a very standard one
import sys

def Hello(name):
    a = 10
    if name == 'Rohan' or name == 'Alice': #logical connectives or/and/not
	print 'Alert: Rohan Mode'
	name = name + '???'
    else:
	#print 'Else'
	DoesNotExisit(name) #program does not run, does not check, so we need test all lines run
    name = name + '!!!'
    print'Hello'+name+str(a)
# Gather our code in a main() function
def main():
    Hello(sys.argv[1])
    #print 'Hello there', sys.argv[1]
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

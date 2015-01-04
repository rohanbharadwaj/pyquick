#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dirname):
  filenames = os.listdir(dirname)
  data_list = []
  for name in filenames:
    m = re.search(r'__\w+__',name)
    if m:
      #print name
      #print os.path.abspath(name)
      data_list.append(os.path.abspath(name))
  #print filenames
  #print data_list
  return data_list

def copy_to(dirname,todir):
  if not os.path.exists(todir):
    os.mkdir(todir)  
  name_list = get_special_paths(dirname)
  for name in name_list:
    fname = os.path.basename(name)
    shutil.copy(name,os.path.join(todir,fname))

def zip_to(dirname, zippath):
  paths = get_special_paths(dirname)
  cmd = 'zip -j '+ zippath + ' '+ ' '.join(paths)
  print "I am going to do : ", cmd
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write(output)
    sys.exit(1)


def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]
    copy_to(args[0],todir)

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]
    zip_to(args[0],tozip)

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  dirname = args[0]
  get_special_paths(dirname)

if __name__ == "__main__":
  main()

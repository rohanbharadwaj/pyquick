pyquick

=======

class link

https://developers.google.com/edu/python/

link for my notes

https://docs.google.com/document/d/1L2zHtovCJU-yKml74QyuWYYKYi-La0OHOqi_RE7qR5Q/edit?usp=sharing

Contents of this project :

    Exercise programs of Googles python tutorial

Notes

-sys.argv[0] ---- program name itself 

-arguments and variables similar no types 

    def Hello(name):

      a = ‘hello’

-print seperate by , then space is includes automatically

-print 'Hello',name,a   ===&gt; Hello rohan!!! 10

-print'Hello'+name+str(a) ⇒ Hellorohan!!!10

-string not empty, num is not 0 -- &gt; true

How python works

-does everything at last possible second

-in the moment it checks at every line 

-strings are immutable (returns new string)

-a.find() - returns first occurance

-a.lower() 

-place holder %

-‘Hi %s I have %d donuts’ %  (‘Alice’,29)

-These are not python strings and not unicode strings these are just series of bytes.

-Strings slice 

&gt;&gt;&gt; a = 'Hello'

&gt;&gt;&gt; a

'Hello'

&gt;&gt;&gt; a[1:3]

'el'

&gt;&gt;&gt; a[1:2]

'e'

&gt;&gt;&gt; a[1:5]

'ello'

&gt;&gt;&gt; a[1:]

'ello'

&gt;&gt;&gt; a[:5]

'Hello'

&gt;&gt;&gt; a[:]

'Hello'

Negatives

--------------------------------------------------------------------------

Lists

-Same syntax across all 

a = [1,2,3,’a’]

-len(a)

-b = a (does not create a copy both point to same)

-lists are mutable

-python has garbage collector {need to make copies is not much}

-a ==b does the same returns true

-slices works fine with lists as well

-There is built in for each

-

for var in list:

   print var

-Check if value in a list {works for lot of DS - in hash table does }

-value in list

-Built in for lists

-append - does not return new list returns None

-a = [1,2,3]

-a.append(4)

-a = a.append(4) # error NO NO

-a.pop(0) pops of element and returns it

-delete a from local scope

del a {complete list}

del a[1]   {delete a element}

-The range(n) function yields the numbers 0, 1, ... 

    for i in range(100)    print i

-sorting of lists - don't use .sort()

-sorted - makes a new list and sorts.

-comparison depends on the type of elements compared.{strings,ints,char}

----------------------------------------------------------------------------------

custom sorting

old way 2 argument comparator method. python has new way

sort by length

&gt;&gt;&gt; sorted(a,key=len)

['d', 'a', 'dc', 'aa', 'ccc']

&gt;&gt;&gt; def last(s): return s[-1]

... 

&gt;&gt;&gt; sorted(a,key=last)

['a', 'aa', 'ccc', 'dc', 'd']

split, join

&gt;&gt;&gt; ':'.join(a)

'z:d:dc:a:aa'

&gt;&gt;&gt; '\n'.join(a)

'z\nd\ndc\na\naa'

&gt;&gt;&gt; ':'.join(a)

'z:d:dc:a:aa'

&gt;&gt;&gt; b = ':'.join(a)

&gt;&gt;&gt; b.split(':')

['z', 'd', 'dc', 'a', 'aa']

Don’t modify list while iterating a list (even java has same constraint)

--------------------------------------------------------------------------------------

Tuple

-Fixed size 

-immutable

-(1,2,3)

-(x,y,z) coordinates; (url,score) {taking fixed number of strings and pass together)

&gt;&gt;&gt; a = (1,3,3)

&gt;&gt;&gt; a

(1, 3, 3)

&gt;&gt;&gt; len(a)

3

&gt;&gt;&gt; a[0]

1

&gt;&gt;&gt; a[0]=2

Traceback (most recent call last):

 File "&lt;stdin&gt;", line 1, in &lt;module&gt;

TypeError: 'tuple' object does not support item assignment

Sort by one thing and then sort by other 

Write key function that returns a tuple

&gt;&gt;&gt; a = [(1,"b"),(2,"a"),(1,"a")]

&gt;&gt;&gt; a

[(1, 'b'), (2, 'a'), (1, 'a')]

&gt;&gt;&gt; sorted(a)

[(1, 'a'), (1, 'b'), (2, 'a')]

Parallel assignment 

&gt;&gt;&gt; (x,y) = (1,2)

--------------------------------------------------------------------------------------

HashTable , /Dictionary

-{}

-key,value bindings

-constant time retrieval 

&gt;&gt;&gt; d ={}

&gt;&gt;&gt; d['a'] = 'alpha'

&gt;&gt;&gt; d['a']

'alpha'

&gt;&gt;&gt; d['B']

Traceback (most recent call last):

 File "&lt;stdin&gt;", line 1, in &lt;module&gt;

KeyError: 'B'

d.get()

&gt;&gt;&gt; d.get('a')

'alpha'

&gt;&gt;&gt; d.get('f')

how to find if something is in dict

‘a’ in d

True

.keys()

&gt;&gt;&gt; d.keys()

['a']

&gt;&gt;&gt; d['b'] = 'beta'

&gt;&gt;&gt; d.keys()

['a', 'b']

values()

&gt;&gt;&gt; d.values()

['alpha', 'beta']

----------looping

&gt;&gt;&gt; for k in sorted(d.keys()): print 'key:',k,'-&gt;',d[k]

... 

key: a -&gt; alpha

key: b -&gt; beta

d.items()

&gt;&gt;&gt; d.items()

[('a', 'alpha'), ('b', 'beta')]

&gt;&gt;&gt; for tuple in d.items(): print tuple

... 

('a', 'alpha')

('b', 'beta')

---------------------------------------------------------------------------------

Files

-----------creating cat python

-f = open(filename,’r’)

-diff modes

-text = f.read()

-lines = f.readlines()

-f.open(fname,”w”)

-f.write(text)   {be careful we can zero out file}

-----------------------------------------------------------------------------------

Regular Expression

-import re

-returns a match object

-match = re.search(pattern,text)

-match = re.search(‘iig’,’its a piiiiiiiig’)

-if match:

-----Imp notations

. dot any character except new line

\w word character

\d digit

\s space

\W everything except that matches \w

\S  everything except that matches \s

 

-left to right once it finds solution it is done 

-if looking for period char

&gt;&gt;&gt; Find('a\.','its a. piiiiiiiig')

a.

raw string 

do not do any special processing with backslashes

uses for writing regex

\S non whitespace

\s whitespace

\d digit 0-9

\w word character a-z A-Z 0-9

------email example

&gt;&gt;&gt; m = re.search(r'([\w.]+)@([\w.]+)','egrreg gjkenrkj@snfjkv.com erngjk @ ')

&gt;&gt;&gt; m

&lt;_sre.SRE_Match object at 0xb7467800&gt;

&gt;&gt;&gt; m.group()

'gjkenrkj@snfjkv.com'

&gt;&gt;&gt; m.group(1)

'gjkenrkj'

&gt;&gt;&gt; m.group(2)

'snfjkv.com'

&gt;&gt;&gt; m = re.search(r'([\w.]+)@([\w.]+)','egrreg gjken.rkj@snfjkv.com erngjk @ ')

&gt;&gt;&gt; m

&lt;_sre.SRE_Match object at 0xb7467140&gt;

&gt;&gt;&gt; m.group(1)

'gjken.rkj'

&gt;&gt;&gt; m.group(2)

'snfjkv.com'

---------findall()

&gt;&gt;re.findall(r'[\w.]+@[\w.]+','egrreg@fmail.com gjken.rkj@snfjkv.com erngjk @ ')

['egrreg@fmail.com', 'gjken.rkj@snfjkv.com']

re.findall(r'([\w.]+)@([\w.]+)','egrreg@fmail.com gjken.rkj@snfjkv.com erngjk @ ')

[('egrreg', 'fmail.com'), ('gjken.rkj', 'snfjkv.com')]

-----flags

DOTALL also matches newline aswell 

how to use constants

&gt;&gt;&gt; m = re.search(r'rohan','ROHAN',re.IGNORECASE)

&gt;&gt;&gt; m

&lt;_sre.SRE_Match object at 0xb726b3d8&gt;

&gt;&gt;&gt; m.group()

'ROHAN'

-------------------------------------------------------------------------------------------

Modules (os,re,urllib,shutil,commands)

1. os module

1. platform independent systime 

2. listdir(path) ----&gt; list of strings

3. os.path.exists(‘/tmp/foo’)

    2. import shutil

shutil.copy(source, dest)   ---- &gt;file copying 

    3. import commands

launch a external process and wait for it to finish

commands.getstatusoutput(cmd)

returns a tuple of length 2 (status,output) 1st int exit code 2nd is all output std output and std error

zip -j name all absolute paths

Exceptions

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

---------------------------------------------------------------------------------------------

Modularity

just .py file namespace 

when we load a python file it runs (do not wrie print outside)

    &gt;&gt;&gt; import babynames

Hi There !!!

&gt;&gt;&gt; dir(babynames)

['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'extract_names', 'main', 're', 'sys']

  &gt;&gt;help(babynames.extract_names)

  

urllib

- Takes url and makes it to look like a file

- import urllib

- Takes a url and tries to look like a file

- uf = urllib.urlopen(‘http://google.com’)

- uf.read()

- has lots of features , set cookies 

&gt;&gt;&gt; urllib.urlretrieve('http://google.com/intl/en_ALL/images/logo.gif','blah.gif')

('blah.gif', &lt;httplib.HTTPMessage instance at 0xb6fa870c&gt;)
Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(getcwd())
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(getcwd())
NameError: name 'getcwd' is not defined
>>> import os
>>> print(os.getcwd())
D:\python
>>> os.chdir('D:\sample projects\python_sample_programs')
>>> print(os.getcwd())
D:\sample projects\python_sample_programs
>>> file=open('mython.py')
>>> str=file.read()
>>> 
>>> print(str)
title="to iterate is human , to recurse divine"

>>> ascii_text="hello, world!"
>>> for i in ascii_text:
...     print(i,ord(i))
... 
...     
h 104
e 101
l 108
l 108
o 111
, 44
  32
w 119
o 111
r 114
l 108
d 100
! 33
>>> unicode_text="Hello, 世界!"
>>> for i in unicode_text:
    print(i, ord(i))

    
H 72
e 101
l 108
l 108
o 111
, 44
  32
世 19990
界 30028
! 33
file=open('mython.py')
file.mode
'r'
file.name
'mython.py'
file.encoding
'cp1252'
file=open('mython.py',encoding='utf-8')
file.encoding
'utf-8'
str=file.read()
str
'title="to iterate is human , to recurse divine"\n'
file.read()
''
file.seek(0)
0
str=file.read()
print(str)
title="to iterate is human , to recurse divine"

print(str)
title="to iterate is human , to recurse divine"

str
'title="to iterate is human , to recurse divine"\n'
str=file.read()
str
''
file.seek(0)
0
file.seek(10)
10
str=file.read()
print(str)
iterate is human , to recurse divine"

file.tell()
49
file.close()
file.closed
True
with open('mython.py',encoding='utf-8') as file:
    file.seek(57)

    
57
home = os.path.expanduser("~")
print(home)
C:\Users\HP
from os.path import expanduser
home=expanduser("~")
print(home)
C:\Users\HP
os.path.dirname(path)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    os.path.dirname(path)
NameError: name 'path' is not defined
os.path.dirname('D:\sample projects\python_sample_programs')
'D:\\sample projects'
os.path.basename('D:\sample projects\python_sample_programs')
'python_sample_programs'
os.walk(top,topdown=True,onerror=None,followlinks=False)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    os.walk(top,topdown=True,onerror=None,followlinks=False)
NameError: name 'top' is not defined
os.path(top, topdown=True, onerror=None, followlinks=False)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    os.path(top, topdown=True, onerror=None, followlinks=False)
NameError: name 'top' is not defined
os.walk(top, topdown=True, onerror=None, followlinks=False)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    os.walk(top, topdown=True, onerror=None, followlinks=False)
NameError: name 'top' is not defined
top="D:\sample projects\python_sample_programs"
os.walk(top, topdown=true, onerror=None, followlinks=False)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    os.walk(top, topdown=true, onerror=None, followlinks=False)
NameError: name 'true' is not defined. Did you mean: 'True'?
top="D:\sample projects\python_sample_programs"
os.walk(top, topdown=True, onerror=None, followlinks=False)
<generator object walk at 0x000001BB68718490>
import os
path="./TEST"
for root,d_names,f_names in os.walk("D:\sample projects\python_sample_programs")
SyntaxError: expected ':'

=== RESTART: D:/sample projects/python_sample_programs/leet_code_problem1.py ===
[1, 2, 3, 0, 0, 0]

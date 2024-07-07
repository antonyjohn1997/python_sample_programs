Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'www.abz.com'.lstrip('wm')
'.abz.com'
'www.aba.com'.lstrip('a')
'www.aba.com'
'www.abc.com'.lstrip('.com')
'www.abc.com'
s="black holes are where God divided by zero"
print(s)
black holes are where God divided by zero
s.partition('are')
('black holes ', 'are', ' where God divided by zero')
s='beetles'
s=s[:3] + 'xx' + s[5:]
s
'beexxes'
s="beetles"
s=s.replace('ee','xx')
s
'bxxtles'
s="black holes are where God divided by zero"
s.rfind(' ')
36
s.rfind('q')
-1
a="banana"
print(a.rfind('a'))
5
print(a.rfind('na'))
4
print(a.rfind('x'))
-1
print(a.rfind('a',0,3))
1
'123'.rjust(10)
'       123'
s="hello, how are you?"
result=s.rpartition(' ')
print(result)
('hello, how are', ' ', 'you?')
s="apple,banana,cherry"
result=s.rsplit(',',1)
print(result)
['apple,banana', 'cherry']
result=s.rsplit()
print(result)
['apple,banana,cherry']
result=s.rsplit( )
print(result)
['apple,banana,cherry']
'   too much right side space     '.rstrip()
'   too much right side space'
'mississippi'.rstrip('im')
'mississipp'
'mississippi'.rstrip('ip')
'mississ'
import re
str="life; a walking, a shadow"
str1=re.split(';|,| ',str)
str1
['life', '', 'a', 'walking', '', 'a', 'shadow']
str2=re.split('; '|, | ',str)
              
SyntaxError: unterminated string literal (detected at line 1)
str2=re.split('; |, | ',str)
              
str2
              
['life', 'a', 'walking', 'a', 'shadow']
SyntaxError: unterminated string literal (detected at line 1)
              
SyntaxError: invalid syntax

s="hello\nworld\r\npython\ris\nawesome"
              
lines=s.splitlines()
              
print(lines)
              
['hello', 'world', 'python', 'is', 'awesome']
s="hello\nworld\r\npython\ris\nawesome"
              
lines=s.splitlines(true)
              
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    lines=s.splitlines(true)
NameError: name 'true' is not defined. Did you mean: 'True'?
lines=s.splitlines(True)
              
print(lines)
              
['hello\n', 'world\r\n', 'python\r', 'is\n', 'awesome']
s="hello, world!"
              
result=s.startswith("hello")
              
print(result)
              
True
result=s.startswith("world",7)
              
print(result)
              
True
#
              
result=s.startswith(("hi","hello"))
              
print(result)
              
True
#strip()
              
s="  hello , world!    "
              
result=s.strip()
              
print(result)
              
hello , world!
s="xxxxyhello, world!  yyy  y"
              
result=s.strip('xy')
              
print(result)
              
hello, world!  yyy  
result=s.strip(' y')
              
print(result)
              
xxxxyhello, world!
result=s.strip('xy y')
              
print(result)
              
hello, world!



# % operator
              
'i am using %s %d.%d' %('python',3,2)
              
'i am using python 3.2'
# Target Syntax Format
              
n=6789
              
a="...%d...%-6d...%06d" % (n,n,n)
              
a
              
'...6789...6789  ...006789'
'%s' % m,str(m)
              
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    '%s' % m,str(m)
NameError: name 'm' is not defined
m=9.876543210
              
'%s' % m,str(m)
              
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    '%s' % m,str(m)
TypeError: 'str' object is not callable
'%s' %m, str(m)
              
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    '%s' %m, str(m)
TypeError: 'str' object is not callable
print('%s' %m, str(m))
              
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print('%s' %m, str(m))
TypeError: 'str' object is not callable

m = 9.876543210
print('%s' % m, str(m))
              
SyntaxError: multiple statements found while compiling a single statement
m = 9.876543210
              
print('%s' % m, str(m))
              
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print('%s' % m, str(m))
TypeError: 'str' object is not callable
m=9.876543210
              
print('%s' % m, str(m))
              
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print('%s' % m, str(m))
TypeError: 'str' object is not callable
print(str)
              
life; a walking, a shadow
del str
              
m=9.876543210
              
print('%s' % m, str(m))
              
9.87654321 9.87654321
'%s' % m
              
'9.87654321'
str(m)
              
'9.87654321'
'%f, %.3f, %.*f' % (9.87654321,9.87654321,4,9.87654321)
              
'9.876543, 9.877, 9.8765'
'%.*f' % (9.87654321)
              
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    '%.*f' % (9.87654321)
TypeError: * wants int
'%.*f' % (4,9.87654321)
              
'9.8765'


#  Formatting dictionary strings
              
'%(m)d %(w)s' % {'m':101, 'w':'freeway'}
              
'101 freeway'
greetings='''Hello %s! Merry Christmas. I hope %d will be a good year.'''
              
replace={'name':'john','year':2024}
              
print(greetings % replace)
              
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    print(greetings % replace)
TypeError: not enough arguments for format string
greetings="hello %(name)s ! Merry Christmas, I hope %(year)d will be a good year"
              
replace={'name':'john','year':2024}
              
print(greetings % replace)
              
hello john ! Merry Christmas, I hope 2024 will be a good year
language="python"
              
version=320
              
vars()
              
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 's': 'xxxxyhello, world!  yyy  y', 'a': '...6789...6789  ...006789', 'result': 'hello, world!', 're': <module 're' from 'D:\\python\\Lib\\re\\__init__.py'>, 'str1': ['life', '', 'a', 'walking', '', 'a', 'shadow'], 'str2': ['life', 'a', 'walking', 'a', 'shadow'], 'lines': ['hello\n', 'world\r\n', 'python\r', 'is\n', 'awesome'], 'n': 6789, 'm': 9.87654321, 'greetings': 'hello %(name)s ! Merry Christmas, I hope %(year)d will be a good year', 'replace': {'name': 'john', 'year': 2024}, 'language': 'python', 'version': 320}
'%(language)s %(version)d ' % vars()
              
'python 320 '


#  String formating by method calls
              

#####Template basics
              
t='{0},{1},{2}'
              
t.format('dec','29','2024')
              
'dec,29,2024'
t='{month}','{day}','{year}'
              
t.format(month='jan',day='30',year='2024')
              
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    t.format(month='jan',day='30',year='2024')
AttributeError: 'tuple' object has no attribute 'format'
>>> t='{month},{day},{year}'
...               
>>> type(t)
...               
<class 'str'>
>>> t.format(month='jan',day='29',year='2024')
...               
'jan,29,2024'
>>> t='{year},{month},{0}'
...               
>>> t
...               
'{year},{month},{0}'
>>> t.format('29',year='2024',month='jan')
...               
'2024,jan,29'
>>> '{month},{year},{0}'.format(month='jan',year='2024','30')
...               
SyntaxError: positional argument follows keyword argument
>>> '{month},{year},{0}'.format('30',month='jan',year='2024')
...               
'jan,2024,30'
>>> ##### Formating with keys and attributes
...               
>>> import sys
>>> 'my {0[machine]} is running {1.platform}'.format({'machine':'samsung'},sys)
'my samsung is running win32'
>>> '{0:10}={1:5}'.format(3.1415,'pi')
'    3.1415=pi   '
>>> ###### working with specific formating
>>> '{0:10}={1:5}'.format(3.1415,'pi')
'    3.1415=pi   '
>>> '{0:e},{1:3e},{2:g},{3:f},{4:.2f},{5:06.2f}.format(3.1415,3.1415,3.1415,3.1415,3.1415,3.1415)
SyntaxError: unterminated string literal (detected at line 1)
>>> '{0:e},{1:3e},{2:g},{3:f},{4:.2f},{5:06.2f}'.format(3.1415,3.1415,3.1415,3.1415,3.1415,3.1415)
'3.141500e+00,3.141500e+00,3.1415,3.141500,3.14,003.14'


UNITS=['KB','MB','GB','TB','PB']
Def sizeinnytes(sz):
    
SyntaxError: invalid syntax
def sizebytes(sz)
SyntaxError: expected ':'

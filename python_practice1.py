Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='black holes are where god divided by zero'
s2='sample.txt'
s.decode()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    s.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
s='aaaaaspybbbbspycccc'
where=s.find('spy')
where
5
s=s[:where]+'SKY'+s[(where+3):]
s
'aaaaaSKYbbbbspycccc'
s="ssss"
s="ssss"
a="hello"
>>> b='hai'
>>> type(a)
<class 'str'>
>>> type(b)
<class 'str'>
>>> s='aaaaaSKYbbbbspycccc'
>>> s.index(where)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s.index(where)
TypeError: must be str, not int
>>> s.index('where')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.index('where')
ValueError: substring not found
>>> where
5
>>> s.index('spy')
12
>>> s.index('one')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    s.index('one')
ValueError: substring not found
>>> s.find('one')
-1
>>> 'abc123'.isalnum()
True
>>> 'abcdef'.isalnum()
True
>>> 'abc def'.isalnum()
False
>>> 'abc'.isalpha()
True
>>> 'abc7'.isalpha()
False
>>> '123'.isdigit()
True
>>> '123a'.isdigit()
False
s
'aaaaaSKYbbbbspycccc'
print(s.islower())
False
s3='hello455'
print(s3.islower())
True
'kkk  kkk'.isspace()
False
'   '.isspace()
True
'  b '.isspace()
False
'b    '.isspace()
False
'black holes'.istitle()
False
'Black Holes'.istitle()
True
'black holes'.isupper()
False
'BLACK HOLES'.isupper()
True
seq=['a','b','c','d']
print ''.join(seq)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(''.join(seq))
abcd
print('-'.join(seq))
a-b-c-d
print(''.join[repr(x) for x in range(101)]
      
SyntaxError: '(' was never closed
print(''.join[repr(x) for x in range[101])
      
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print(''.join[repr(x) for x in range(101)])
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(' '.join[repr(x) for x in range(101)])
      
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(''.join([repr(x) for x in range(101)]))
      
0123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869707172737475767778798081828384858687888990919293949596979899100
123.ljust(10,'--')
      
SyntaxError: invalid decimal literal
'123'.ljust(10,'-')
      
'123-------'
string="conVERT ALL TO LOWWERCASE"
      
print(string.lower())
      
convert all to lowwercase




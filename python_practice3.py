Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
##### Python files and Os.path
import os
print(os.path.join('/test/','myfile'))
/test/myfile
print(os.path.join(os.path.expanduser('~'))
... 
... 
... 
... 
... 
... 
... 
... import os
...       
SyntaxError: '(' was never closed
>>> import os
...       
>>> print(os.path.join('/test/','/myfile'))
...       
/myfile
>>> pathname = "/Users/K/dir/subdir/k.py"
...       
>>> os.path.split(pathname)
...       
('/Users/K/dir/subdir', 'k.py')
>>> (dirname,filename) = os.path.split(pathname)
...       
>>> pathname
...       
'/Users/K/dir/subdir/k.py'
>>> dirname
...       
'/Users/K/dir/subdir'
>>> filename
...       
'k.py'
>>> pathname
...       
'/Users/K/dir/subdir/k.py'
>>> (shortname, extension) = os.path.splitext(filename)
...       
>>> shortname
...       
'k'
>>> extension
      
'.py'
import glob
      
matching_files=glob.glob('subdir/*.py')
      
import glob
matching_files=glob.glob('subdir/*.py')
import glob
os.chdir('/test')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    os.chdir('/test')
FileNotFoundError: [WinError 2] The system cannot find the file specified: '/test'
import glob
os.chdir('/test')
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    os.chdir('/test')
FileNotFoundError: [WinError 2] The system cannot find the file specified: '/test'
import glob
glob.glob('subdir/*.py')
[]
metadata=os.stat('test1.py')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    metadata=os.stat('test1.py')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'test1.py'
metadata=os.stat('script1.py')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    metadata=os.stat('script1.py')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'script1.py'
python script1.py
SyntaxError: invalid syntax
import os
print(os.getcwd())
D:\python
os.chdir('D:\sample projects\python_sample_programs')
print(os.getcwd())
D:\sample projects\python_sample_programs
metadata=os.stat('strict.py')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    metadata=os.stat('strict.py')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'strict.py'
print(os.getcwd())
D:\sample projects\python_sample_programs
metadata=os.stat('D:\sample projects\python_sample_programs')

metadata=os.stat('strict1.py')
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    metadata=os.stat('strict1.py')
FileNotFoundError: [WinError 2] The system cannot find the file specified: 'strict1.py'
metadata=os.stat('D:\sample projects\python_sample_programs')
metadata.st_mtime
1717648312.8983572
print("File size:",metadata.st_size,"bytes")
File size: 4096 bytes
metadata=os.stat('mython.py')
metadata.st_mtime
1717263639.50674
print("filesize:",metadata.st_size,"bytes")
filesize: 49 bytes
import time
time.localtime(metadata.st_mtime)
time.struct_time(tm_year=2024, tm_mon=6, tm_mday=1, tm_hour=23, tm_min=10, tm_sec=39, tm_wday=5, tm_yday=153, tm_isdst=0)
metadata.st_size
49
print(os.path.realpath('mython.py')



 zz
      
SyntaxError: '(' was never closed
print(os.path.realpath('mython.py'))
      
D:\sample projects\python_sample_programs\mython.py
import os
os.environ['SUBDIR']='subdir'
print(os.path.expandvars('/home/users/K/$SUBDIR'))
/home/users/K/subdir
print(o.getcwd())
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    print(o.getcwd())
NameError: name 'o' is not defined. Did you mean: 'os'?
import os
print(os.getcwd())
D:\sample projects\python_sample_programs
myfile=open('mydir/myfile.txt', 'w' ')
            
SyntaxError: unterminated string literal (detected at line 1)
myfile = open('mydir/myfile.txt')
            
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    myfile = open('mydir/myfile.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mydir/myfile.txt'
os.directry()
            
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    os.directry()
AttributeError: module 'os' has no attribute 'directry'. Did you mean: 'DirEntry'?
import os
os.getforward()
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    os.getforward()
AttributeError: module 'os' has no attribute 'getforward'
import os
myfile=open('mydir/myfile.txt','w')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    myfile=open('mydir/myfile.txt','w')
FileNotFoundError: [Errno 2] No such file or directory: 'mydir/myfile.txt'
import os
myfile=open('D:\sample projects\python_sample_programs','w')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    myfile=open('D:\sample projects\python_sample_programs','w')
PermissionError: [Errno 13] Permission denied: 'D:\\sample projects\\python_sample_programs'

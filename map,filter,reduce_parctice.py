Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[x for x in range(10) if x%2==0]
>>> l
[0, 2, 4, 6, 8]
>>> m=filter(lambda x:x % 2 == 0, [x for x in range[10]])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    m=filter(lambda x:x % 2 == 0, [x for x in range[10]])
TypeError: type 'range' is not subscriptable
>>> m=filter(lambda x:x % 2 == 0, [x for x in range(10)])
>>> m
<filter object at 0x000002529BD08220>
>>> m= list(filter(lambda x:x % 2 == 0, [x for x in range(10)]))
>>> print(m)
[0, 2, 4, 6, 8]
>>> m=list(map(lambda x:x % 2 == 0, [x for x in range(10)]))
>>> m
[True, False, True, False, True, False, True, False, True, False]
>>> number=[1,2,3,4]
>>> squared=list(map(lambda x: x**2,number))
>>> squared
[1, 4, 9, 16]
>>> number=[1,2,3,4]
>>> squared=map(lambda x: x**2,number)
>>> squared
<map object at 0x000002529BD08220>
>>> squared=list(map(lambda x: x**2,number))
>>> squared
[1, 4, 9, 16]
>>> 
>>> 
>>> import functools
>>> numbers=[1,2,3,4,5]
>>> sum=functools.reduce(lambda x,y: x+y, numbers)
>>> sum
15
>>> 
>>> 
>>> #### above filter(),map(),reduce() ####
>>> 

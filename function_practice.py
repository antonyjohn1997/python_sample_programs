Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ##### functions #####
>>> 
>>> def square():
...     new_value=4**2
...     print(new_value)
... 
...     
>>> square()
16
>>> 
>>> #### function parameters ####
>>> 
>>> def square(value):
...     new_value=value**2
...     print(new_value)
... 
...     
>>> square(5)
25
>>> square(100)
10000
>>> 
>>> 
>>> #### return values from function####
>>> 
>>> def square(value):
...     new_value=value**2
...     return new_value
... 
>>> num=square(4)
>>> print(num)
16
>>> 
>>> object1="data" + "analysis" + "visualization"
>>> object2=1 * 3
>>> object3="1" * 3
>>> print(object1)
dataanalysisvisualization
print(object2)
3
print(object3)
111


x=5.5
type(x)
<class 'float'>
y1:y1=str(x)
type(y1)
<class 'str'>
y2:y2=print(x)
5.5
type(y2)
<class 'NoneType'>
def shout():
    shout_word="congratulations"
    print(shout_word+"!!!")

    
shout()
congratulations!!!



#### function with parameter ###

def shout(word):
    shout_word = word + "!!!"
    print(shout_word)

    
shout("congratulations")
congratulations!!!
shout("hai")
hai!!!


### function that return single values ###

def shout(word):
    shout_word=word+"!!!" ### concatenate strings
    return shout_word
yell=shout("congratulations")## pass 'congratulations' to shout:yell
SyntaxError: invalid syntax
yell=shout("congratulations")
congratulations!!!
print(yell)
None
type(yell)
<class 'NoneType'>
print(yell=shout("congratulations"))
congratulations!!!
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print(yell=shout("congratulations"))
TypeError: 'yell' is an invalid keyword argument for print()
print(yell)
None



### multiple function parameter ###

def raise_to_power(value1,value2):
    """ raise value1 to the power of value2 """
    new_value=value1 ** value2
    return new_value

result=raise_to_power(2,3)
print(result)
8


##tuples

even_nums=(2,4,6)
print(type(even_nums))
<class 'tuple'>
a,b,c =even_nums
print(a)
2
print(b)
4
print(c)
6
### above unpacking tuples

#### we can access tuple elements like do with list ####

print(even_nums[1])
4
print(even_nums[2])
6

#### returning xple values ###

def raise_both(value1,value2):
    """ raise value1 to the power of value2 and vice versa """
    new_value1=value1**value2
    new_value2=value2**value1
    new_tuple=(new_value1,new_value2)
    return(new_value1,new_value2)

    
result=raise_both(5,2)
print(result)
(25, 32)


### funtions with xple parameters ###

def shout(word1,word2):
    ##concatenate word1 with '!!!'
    shout1=word1+"!!!"
    ## concatenate word2 with '!!!'
    shout2=word2+"!!!"
    ##concatenate shout1 with shout2
    new_shout=shout1+shout2
    return new_shout
yell=shout("congratulations","you")
SyntaxError: invalid syntax
yell=shout("congratulations","you")
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    yell=shout("congratulations","you")
TypeError: shout() takes 1 positional argument but 2 were given
shout("congratulations","you")
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    shout("congratulations","you")
TypeError: shout() takes 1 positional argument but 2 were given

= RESTART: D:/sample projects/python_sample_programs/fns_with_xple_parameter.py
congratulations!!!you!!!


### brief introduction to tuple
### Unpack nums to the variables num1, num2, and num3.##Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.
print(nums)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    print(nums)
NameError: name 'nums' is not defined
nums=(3,4,6)
print(nums)
(3, 4, 6)
type(nums)
<class 'tuple'>
print(nums[1])
4
num1,num2,num3=nums##unpacking
nums[0]=2
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    nums[0]=2
TypeError: 'tuple' object does not support item assignment
## we cant change tuple values
even_nums=(2,num2,num3)##Construct a new tuple, even_nums composed of the same elements in nums, but with the 1st element replaced with the value, 2.
print(even_nums)
(2, 4, 6)

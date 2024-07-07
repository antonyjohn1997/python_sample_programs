Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
hall=11.25
kit=18.0
liv=20.2
bed=5
bath=9
areas=["hallway",hall,"kitchen",kit,"living room",liv,"bedroom",bed,"bathroom",bath]
print(areas)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2, 'bedroom', 5, 'bathroom', 9]
#list

a=[1,2,4,3]
type(a)
<class 'list'>
b=[[1,2,3],[4,5,7]]
print(b)
[[1, 2, 3], [4, 5, 7]]
type(b)
<class 'list'>
c=[1+2,"a"*5,3]
print(c)
[3, 'aaaaa', 3]
type(c)
<class 'list'>

#list_of_list

hall=22
kit=5.0
liv=88.3
bed=6
bath=6.3
  # variables declared
  
house=[["hallway",hall],["kitchen",kit],["living room",liv],["bedroom",bed],["bathroom",bath]]
print(house)
[['hallway', 22], ['kitchen', 5.0], ['living room', 88.3], ['bedroom', 6], ['bathroom', 6.3]]


#     Subsetting List

area=["hallway",11.25,"kitchen",18.0,"living room",20.2,"bedroom",10.75,"bathroom",9.50]
print(area[1])
11.25
print(area(-1))
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(area(-1))
TypeError: 'list' object is not callable
print(area[-1])
9.5
print(area[5])
20.2
print(area[hallway])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print(area[hallway])
NameError: name 'hallway' is not defined
print(area["hallway"])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(area["hallway"])
TypeError: list indices must be integers or slices, not str
print(area[0])
hallway
areas=["hallway",11.25,"kitchen",18.0,"living room",20.2,"bedroom",10.75,"bathroom",9.50]
eat_sleep_area=areas[3]+areas[-3]
print(eat_sleep_area)
28.75
kit_bed=areas[2]+areas[6]
print(kit_bed)
kitchenbedroom
kit_bed=areas[2]+" "+areas[6]
print(kit_bed)
kitchen bedroom
print(areas)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2, 'bedroom', 10.75, 'bathroom', 9.5]
downstairs=areas[0:6]
print(downstairs)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2]
upstairs=areas[-4:]#slicing
print(upstairs)
['bedroom', 10.75, 'bathroom', 9.5]
upstairs2=areas[:-4]
print(upstairs2)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2]
print(areas[-10])
hallway
print(areas[-4:-10])
[]
print(areas[-10:-4])
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2]
downstairs=areas[:6]
print(downstairs)
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2]
upstairs=areas[-4:]
print(upstairs)
['bedroom', 10.75, 'bathroom', 9.5]
upstairs=4
print(upstairs)
4


##What will house[-1][1] return?
house[-1][1]
6.3
print(house)
[['hallway', 22], ['kitchen', 5.0], ['living room', 88.3], ['bedroom', 6], ['bathroom', 6.3]]

####          subsetting list of lists
##
x=[["a","b","c"],]


x=[["a","b","c"],["d","e","f"],["g","h","i"]]
x[2][0]
'g'
x[2]
['g', 'h', 'i']
x[2][:3]
['g', 'h', 'i']



#######    Replacing list elements

areas
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2, 'bedroom', 10.75, 'bathroom', 9.5]
areas[-1]=10.50
areas
['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.2, 'bedroom', 10.75, 'bathroom', 10.5]
areas[4]="chill zone"
areas
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5]
x
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
z=["a","b","c","d"]
x[1]="r"
x[2:]=["s","t"]
x
[['a', 'b', 'c'], 'r', 's', 't']
del x
x
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    x
NameError: name 'x' is not defined
z
['a', 'b', 'c', 'd']
z[1]="r"
z
['a', 'r', 'c', 'd']
z[2:]=["s","t"]
z
['a', 'r', 's', 't']
#### extend a list
areas
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5]
areas_1=areas + ["poolhouse",24.5]
areas_1
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5]
areas_2=areas_1+["garage",15.25]
areas_2
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5, 'garage', 15.25]
##deleting list element
areas
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5]
areas_2
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5, 'garage', 15.25]
del(areas[-4:-2])
areas_2
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5, 'poolhouse', 24.5, 'garage', 15.25]
areas
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bathroom', 10.5]
del(areas_2[-4:-2])
areas_2
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5, 'garage', 15.25]
list(areas_2)
['hallway', 11.25, 'kitchen', 18.0, 'chill zone', 20.2, 'bedroom', 10.75, 'bathroom', 10.5, 'garage', 15.25]
## inner working list
areas=[11.25,18.0,20.0,10.75,9.50]
areas_copy=list(areas)
print(areas_copy)
[11.25, 18.0, 20.0, 10.75, 9.5]
areas_copy[0]=5.0
print(areas)
[11.25, 18.0, 20.0, 10.75, 9.5]
print(areas_copy)
[5.0, 18.0, 20.0, 10.75, 9.5]
areas_copy2=areas_copy1
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    areas_copy2=areas_copy1
NameError: name 'areas_copy1' is not defined. Did you mean: 'areas_copy'?
areas_copy2=areas_copy
print(areas_copy2)
[5.0, 18.0, 20.0, 10.75, 9.5]
print(areas_copy)
[5.0, 18.0, 20.0, 10.75, 9.5]
areas_copy[0]=8
areas_copy
[8, 18.0, 20.0, 10.75, 9.5]
areas_copy2
[8, 18.0, 20.0, 10.75, 9.5]



#####    Functions

##built in functions

var1=[1,2,3,4]
var2=True

print(type(var1))
<class 'list'>
print(len(var1))
4
out2=int(var2)
print(out2)
1
var3=False
print(int(var3))
0
first=[11.25,18.0,20.0]
second=[10.75,9.50]
full=first + second
print(full)
[11.25, 18.0, 20.0, 10.75, 9.5]
full_sorted=sorted(full,reverse=True)
print(full_sorted)
[20.0, 18.0, 11.25, 10.75, 9.5]
full_sorted=sorted(full,reverse=False)
print(full_sorted)
[9.5, 10.75, 11.25, 18.0, 20.0]
print(max(full_sorted))
20.0
print(round(10.75))
11
print(round(10.75,1))
10.8
place="poolhouse"
place_up=place.upper()
print(place_up)
POOLHOUSE
print(place)
poolhouse
print(place.count("o"))
3
print(place.count(0))
Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    print(place.count(0))
TypeError: must be str, not int
print(place.count("0"))
0
areas=[11.25,18.0,20.0,10.75,9.50]
print(areas.index(20.0))
2
print(areas.count(9.50))
1




###########List Methods


areas=[11.25,18.0,20.0,10.75,9.50]
areas.append(24.5)
print(areas)
[11.25, 18.0, 20.0, 10.75, 9.5, 24.5]
areas.append(15.5))
SyntaxError: unmatched ')'
areas.append(15.25)
print(areas)
[11.25, 18.0, 20.0, 10.75, 9.5, 24.5, 15.25]
areas.reverse()
print(areas)
[15.25, 24.5, 9.5, 10.75, 20.0, 18.0, 11.25]
a=[5,8,55,6]
print(a.reverse())
None
a.append(23)
print(a)
[6, 55, 8, 5, 23]
a.reverse()
a
[23, 5, 8, 55, 6]
a.append(99)
a
[23, 5, 8, 55, 6, 99]
a.reverse()
a
[99, 6, 55, 8, 5, 23]
a.remove(99)
a
[6, 55, 8, 5, 23]



>>> 
>>> ######package
>>> 
>>> import math
>>> r=0.43
>>> c=2*math.pi*r
>>> a=math.pi*r**2
>>> print("circumstance:"+str(c))
circumstance:2.701769682087222
>>> print("area"+str(a))
area0.5808804816487527
>>> print(c)
2.701769682087222
>>> 
>>> 
>>> from math import pi
>>> from math import radians
>>> 
>>> r=192500
>>> dist=r*radians(12)
>>> print(dist)
40317.10572106901
>>> 
>>> 
>>> 
>>> 
>>> ######## numpy
>>> 
>>> import numpy as np
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
>>> numpy
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    numpy
NameError: name 'numpy' is not defined
>>> import numpy as np

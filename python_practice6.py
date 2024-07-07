Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
########Numpy

import numpy as np
baseball=[180,215,210,210,188,176,209,200]
np_baseball=np.array(baseball)
print(np_baseball)
[180 215 210 210 188 176 209 200]
print(type(np_baseball))
<class 'numpy.ndarray'>
height_inch=[74,74,72,70,75,75,73]
np_height_inch=np.array(height_inch)
np_height_meter=np_height_inch*0.0254
print(np_height_meter)
[1.8796 1.8796 1.8288 1.778  1.905  1.905  1.8542]
print(type(np_height_meter))
<class 'numpy.ndarray'>


###bmi

import numpy as np
height_m=[159.5,130.8,180.8,178.6,200,201]
height_meter=np.array(height_m)*0.254
print(height_m)
[159.5, 130.8, 180.8, 178.6, 200, 201]
print(height_meter)
[40.513  33.2232 45.9232 45.3644 50.8    51.054 ]
weight_lb=[52.3,50,100,80,60.3,88.55]
weight_kg=np.array(weight_lb)*0.453592
print(weight_kg)
[23.7228616 22.6796    45.3592    36.28736   27.3515976 40.1655716]
10/2
5.0
10**2
100
10**3
1000
bmi=weight_kg/(height_meter**2)
print(bmi)
[0.01445367 0.02054719 0.02150805 0.01763295 0.01059877 0.01540971]
light=bmi<30
print(light)
[ True  True  True  True  True  True]
np_light=np.array(light)
print(np_light)
[ True  True  True  True  True  True]
####array should be True if the corresponding baseball player's BMI is below 30, that is light and np_light.
####printing the array of bmis of all players whose bmi is below 30
print(bmi[bmi<30])
[0.01445367 0.02054719 0.02150805 0.01763295 0.01059877 0.01540971]
np_bmi=np.array(bmi)
print(np_bmi)
[0.01445367 0.02054719 0.02150805 0.01763295 0.01059877 0.01540971]
print(weight_kg[3])
36.28736
print(height_meter[1:4])
[33.2232 45.9232 45.3644]
### some properties of list and numpy array are same .

#####2d numpy array


baseball=[[180,78.4],[215,102.7],[210,98.5],[188,75.2]]
print(baseball)
[[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
np_baseball=np.array(baseball)
print(np_baseball)
[[180.   78.4]
 [215.  102.7]
 [210.   98.5]
 [188.   75.2]]
## here all elements are changed to float type

print(type(np_baseball))
<class 'numpy.ndarray'>
print(np_baseball.shape)
(4, 2)
print(np_baseball[1:])
[[215.  102.7]
 [210.   98.5]
 [188.   75.2]]
print(np_baseball[:,1])
[ 78.4 102.7  98.5  75.2]
print(np_baseball[1,: ])
[215.  102.7]
print(np_baseball[1][2])
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(np_baseball[1][2])
IndexError: index 2 is out of bounds for axis 0 with size 2
print(np_baseball[1][1])
102.7
print(np_baseball[4][1])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(np_baseball[4][1])
IndexError: index 4 is out of bounds for axis 0 with size 4
print(np_baseball[3][1])
75.2


####2d arithmetic
import numpy as np
np_baseball_2=np.array([[180,78.4],[241,102.7],[210,98.5],[188,75.2]])
print(np_baseball_2)
[[180.   78.4]
 [241.  102.7]
 [210.   98.5]
 [188.   75.2]]
cricket=np.array([[5,.5],[5,.5],[5,.5],[5,.5]])
print(cricket)
[[5.  0.5]
 [5.  0.5]
 [5.  0.5]
 [5.  0.5]]
result=np_baseball_2+cricket
print(result)
[[185.   78.9]
 [246.  103.2]
 [215.   99. ]
 [193.   75.7]]
conversion=np.array([0.0254,0.453592])
result_2=np_baseball*conversion
print(result_2)
[[ 4.572     35.5616128]
 [ 5.461     46.5838984]
 [ 5.334     44.678812 ]
 [ 4.7752    34.1101184]]
baseball
[[180, 78.4], [215, 102.7], [210, 98.5], [188, 75.2]]
height_meter
array([40.513 , 33.2232, 45.9232, 45.3644, 50.8   , 51.054 ])
print(height_meter)
[40.513  33.2232 45.9232 45.3644 50.8    51.054 ]
print(height_meter.shape)
(6,)


#####avg

np_baseball_in=np.array(np_baseball[:,0])
print(np_baseball_in)
[180. 215. 210. 188.]
np_baseball
array([[180. ,  78.4],
       [215. , 102.7],
       [210. ,  98.5],
       [188. ,  75.2]])
print(np.mean(np_baseball_in))
198.25
print(np.median(np_baseball_in))
199.0
>>> 
>>> avg=np.mean(np_baseball[:,0])
>>> print("average:"+str(avg))
average:198.25
>>> median=np.median(np_baseball[:,0])
>>> print("median :"+str(median))
median :199.0
>>> stddev=np.std(np_baseball[:,0])
>>> print("standard deviation:"+str(stddev))
standard deviation:14.635146053251399
>>> corr=np.corrcoef(np_baseball[:,0],np_baseball[:,1])
>>> print("correlation:"+str(corr))
correlation:[[1.         0.95865738]
 [0.95865738 1.        ]]
>>> positions=["gk","k",55,88,2.2,"hai"]
>>> np_positions=np.array(positions)
>>> print(np_positions)
['gk' 'k' '55' '88' '2.2' 'hai']
>>> baseball_height
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    baseball_height
NameError: name 'baseball_height' is not defined
>>> height_meter
array([40.513 , 33.2232, 45.9232, 45.3644, 50.8   , 51.054 ])
>>> gk_heights=np_positions[np_positions=='gk']
>>> print(gk_heights)
['gk']
>>> gk__heights=height_meter[np_positions=='gk']
>>> print(gk__heights)
[40.513]
>>> others=height_meter[np_positions!=='gk']
SyntaxError: invalid syntax
>>> others=height_meter[np_positions!='gk']
>>> print(others)
[33.2232 45.9232 45.3644 50.8    51.054 ]
>>> print(np_positions!='gk')
[False  True  True  True  True  True]

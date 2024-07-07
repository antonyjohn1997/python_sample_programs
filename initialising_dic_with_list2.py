L=[1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]
from collections import defaultdict
d=defaultdict(list)
for i in L:
    d[len(str(i))].append(i)
print(d)
print({k:v for k,v in d.items()})

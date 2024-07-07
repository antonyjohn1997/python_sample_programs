cities={'San Francisco':'US','London':'UK','Manchester':'UK','Paris':'France','Los Angels':'US','Seoul':'Korea'}
from collections import defaultdict
d1=defaultdict(list)
print(d1)
print(cities)

#a=cities.items()
#print("cities.items()",a)

#print(cities['Paris'])
d2={}
for k, v in cities.items():
    print("d1:",d1)
    print(k,v)
    d1[v].append(k)#or
    d2.setdefault(v,[]).append(k)
    #print(d1[v].append(k))


#print(d1) or
print(f'd1={d1}')
print(f"d2={d2}")


cities={'San Francisco':'US','London':'UK','Manchester':'UK','Paris':'France','Los Angeles':'US','Seoul':'Korea'}
cities
a=[v for k,v in cities.items()]
print(a)
ds={x:[] for x in set(a)}
print(ds)
for k,v in cities.items():
    ds[v].append(k)

print(ds)    

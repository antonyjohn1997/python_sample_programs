ss = """Nory was a Catholic because her mother was a Catholic, 
and Nory's mother was a Catholic because her father was a Catholic, 
and her father was a Catholic because his mother was a Catholic, 
or had been."""

words = ss.split()
d = {}.fromkeys(words,0)

# or we can use this to initialize a dict
d = {x:0 for x in words}

for w in words:
    d[w] += 1
print(d)

ds=sorted(d.items(),key=lambda x: x[1], reverse=True)
print(ds)


# or we can use this for the key
#import operator
#ds2 = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
#print(ds2)

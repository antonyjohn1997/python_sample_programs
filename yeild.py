#def foo_with_yield():
    #yield 1
    #yield 6
    #yield 10


#for yield_value in foo_with_yield():
    #print(yield_value, end=" ")    
#################################################

#def hello():
    #return [1,2,3]
    #return 5
    #return [1,2,3]
#result=hello()
#print(result)

###################################################
    
def repeat5times(x):
    for c in x:
        yield c * 5


s=repeat5times("abc")
print(s)
for item in s:
    print(item)



################################################


def simple_generator():
    yield 1
    yield 2
    yield 3

# Create a generator object
gen = simple_generator()
print(gen)

# Use next() to get values one at a time
print(next(gen))  # Outputs: 1
print(next(gen))  # Outputs: 2
print(next(gen))  # Outputs: 3

# Calling next() again will raise StopIteration as the generator is exhausted
# print(next(gen))  # Raises StopIteration
    




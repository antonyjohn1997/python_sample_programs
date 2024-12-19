my_dict={}
my_dict={1:'apple',2:'banana'}#dictionary with integer keys

my_dict={'name':'John','age':25,3:[1,2,3]}#dictionary with mixed keys
print(my_dict)

#accessing values

my_dict={'name':'Alice','age':30,'city':'New York'}
print(my_dict['name'])
print(my_dict['age'])


#modifying values
my_dict['age']=31
print(my_dict)


#adding key value pair
my_dict['country']='USA'
print(my_dict)


#removing Key value pair

age=my_dict.pop('age')
print(age)
print(my_dict)

del my_dict['city']
print(my_dict)


#looping through dictionary

#keys

for key in my_dict:
    print(key)

#values
    for value in my_dict.values():
        print(value)
    #print(kk)    


#key-value pair

for key,value in my_dict.items():
            print(key,value)

my_dict['salary']=100
print(my_dict.items())           

print(my_dict)
            
for value in my_dict.values():
    print(value)


#dictionary Comprehension

squares={x:x**2 for x in range(5)}
print(squares)


#merging dictionaries

dict1={'a':1, 'b':2}
dict2={'b':3, 'c':4}

#using update()
dict1.update(dict2)
print(dict1)

#using | operator

merged_dict=dict1 | dict2
print(merged_dict)


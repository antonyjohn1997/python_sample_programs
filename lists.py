#creating lists
my_list=[]
my_list=[1,2,3,4,5]
my_list=[1,"hello",3.14,True]

#accessing Elemnts
my_list=[1,2,3,4,5]
print(my_list[1])
print(my_list[2])
print(my_list[-1])

#modifying Elements

my_list[2]=12
print(my_list)

#adding Elemts
#append
my_list.append(4)
print(my_list)

#insert
my_list.insert(1,"a")
print(my_list)

#extend
my_list.extend([4,5,6])
print(my_list)

#removing elemnts
my_list.remove(2)
print(my_list)
my_list.remove(4)# removes first occurence of a specified elemnt
print(my_list)


removed_element=my_list.pop(2)
print(removed_element)
print(my_list)

#slicing lists

sliced_list=my_list[1:4]
print(sliced_list)

#looping through list

for item in my_list:
    print(item)

#list comprehension

    squares=[x**2 for x in range(5)]
    print(squares)
    

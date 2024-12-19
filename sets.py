my_set={1,2,3}
my_set=set()

my_set = set([1,2,3,4,4,2])
print(my_set)

#adding elemnts

my_set={1,2,3}
my_set.add(4)
print(my_set)


my_set.update([5,6,7])
print(my_set)


# removing elemnts

my_set.remove(2)
print(my_set)
my_set.discard(10)


element = my_set.pop()
print(element)
print(my_set)

#set operations

set1={1,2,3}
set2={3,4,5}
union_set=set1 | set2
print(union_set)


#intersection

intersection_set =set1 & set2
print(intersection_set)


#difference

difference_set=set1 - set2
print(difference_set)

#symmetric_difference_set

symmetric_difference_set=set1^set2
print(symmetric_difference_set)

#membership testing
my_set={1,2,3,4,5}
print(3 in my_set)
print(10 in my_set)

#looping throgh set

my_set={1,2,3,4,5}
for item in my_set:
    print(item)

Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ###Lists####
>>> prices=[10,20,30,15,25,35]
>>> prices[::2]
[10, 30, 25]
>>> prices[1::3]
[20, 25]
>>> list[1,"Blindng Light",2,"One Dance",3,"Uptown Funk"]
list[1, 'Blindng Light', 2, 'One Dance', 3, 'Uptown Funk']
>>> print(list)
<class 'list'>
>>> playlist=[1,"Blinding Light",2,"One Dance",3,"Uptown Funk"]
>>> print(playlist)
[1, 'Blinding Light', 2, 'One Dance', 3, 'Uptown Funk']
>>> print(playlist[4])
3
>>> print(-1)
-1
>>> print(playlist[-1])
Uptown Funk
>>> ###print every song in the playlist###
>>> print(::2)
SyntaxError: invalid syntax
>>> print(playlist[::2])
[1, 2, 3]
>>> print(playlist[1::2])
['Blinding Light', 'One Dance', 'Uptown Funk']
>>> 
>>> 
>>> #### dictionary####
>>> 
>>> products_dict = {"AG32":10,"HT91":20,"PL65":30,"OS31":15,"KB07":25,"TR48":35}
>>> type(product_dict)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    type(product_dict)
NameError: name 'product_dict' is not defined. Did you mean: 'products_dict'?
>>> print(type(products_dict))
<class 'dict'>
print(products_dict["AG32"])
10
print(products_dict.values())
dict_values([10, 20, 30, 15, 25, 35])
print(products_dict.keys())
dict_keys(['AG32', 'HT91', 'PL65', 'OS31', 'KB07', 'TR48'])
print(products_dict)
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35}
print(products_dict.items())
dict_items([('AG32', 10), ('HT91', 20), ('PL65', 30), ('OS31', 15), ('KB07', 25), ('TR48', 35)])
products_dict["UI56"]=40
print(products_dict)
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35, 'UI56': 40}
products_dict["533.23AB":2333]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    products_dict["533.23AB":2333]
KeyError: slice('533.23AB', 2333, None)
products_dict["523.23AB"]=52
print(products_dict)
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35, 'UI56': 40, '523.23AB': 52}
products_dict["523.23AB"]=100
print(products_dict)
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35, 'UI56': 40, '523.23AB': 100}
products_dict["AG32"]=10
print(product_dict)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print(product_dict)
NameError: name 'product_dict' is not defined. Did you mean: 'products_dict'?
print(products_dict)
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35, 'UI56': 40, '523.23AB': 100}
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35, 'UI56': 40, '523.23AB': 100}
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35, 'UI56': 40, '523.23AB': 100}
playlist={"The weekend":"Blinding lights","drake":"one dance"}
print(playlist)
{'The weekend': 'Blinding lights', 'drake': 'one dance'}
playlist["Usher"]="Yeah"
print(playlist.values())
dict_values(['Blinding lights', 'one dance', 'Yeah'])


####sets###
attendees_set={"John Smith","Alan Jones","Rojer Thompson","John Smith","Brandon Sharp","Sam Washington"}
print(attendees_set)
{'John Smith', 'Rojer Thompson', 'Brandon Sharp', 'Alan Jones', 'Sam Washington'}
#existing list variable
attendees_list=["John Smith","Alan Jones","Rojer Thompson","John Smith","Brandon Sharp","Sam Wasington"]
#convert to a set
attendees_set=set(attendees_set)
print(attendees_list)
['John Smith', 'Alan Jones', 'Rojer Thompson', 'John Smith', 'Brandon Sharp', 'Sam Wasington']
print(attendees_set)
{'John Smith', 'Rojer Thompson', 'Brandon Sharp', 'Alan Jones', 'Sam Washington'}
type(attendees_set)
<class 'set'>
sorted_attendees_set=sorted(attendees_set)
print(sorted_attendees_set)
['Alan Jones', 'Brandon Sharp', 'John Smith', 'Rojer Thompson', 'Sam Washington']
print(type(sorted_attendees_set))
<class 'list'>
print(type(sorted_attendees_set))## sorted returns list
<class 'list'>


#### creating a tuple ####

office_locations=("new york city","london","leoven")
print(office_locations)
('new york city', 'london', 'leoven')
### convert another data structure to a tuple ###
print(attendees_list)
['John Smith', 'Alan Jones', 'Rojer Thompson', 'John Smith', 'Brandon Sharp', 'Sam Wasington']
print(type(attendees_list))
<class 'list'>
attendees=tuple(attendees_list)
print(attendees)
('John Smith', 'Alan Jones', 'Rojer Thompson', 'John Smith', 'Brandon Sharp', 'Sam Wasington')
print(type(attendees))
<class 'tuple'>
print(office_locations[2])###access 3rd element
leoven
hip_hop=["Drake","Jay-z","50 Cent","Drake"]
type(hip_hop)
<class 'list'>
indie_set={"Kings of Leon","MGMT","Stereophonics"}### create set
type(indie_set)
<class 'set'>
hip_hop_set=set(hip_hop)##convert hip_hop to a set
print(hip_hop_set)
{'Jay-z', '50 Cent', 'Drake'}
type(hip_hop_set)
<class 'set'>


#### control flow and looops

inflation_september=123.321
inflation_august=321.123
if inflation_september < inflation_august:
    print("Inflation decreased")
elif inflation_september > inflation_august:
    print("inflation increased")
else:
    print("Inflation remained stable")

    
Inflation decreased


### if

num_beds=120
min_num_beds=50
sq_foot=53
min_sq_foot=22
rent=1000
max_rent=3000

if num_beds < min_num_beds:
    print("Insufficient bedrooms")
elif sq_foot <= min_sq_foot:
    print("Too small")
elif rent > max_rent:
    print("Too expensive")
else:
    print("This looks promising!")

    
This looks promising!

### for loop

user_ids=["abc1","abc2","abc3","abc4","abc5"]
for i in user_ids:
    print(i)

    
abc1
abc2
abc3
abc4
abc5


tickets_sold=0
max_capacity=50
for i in range(1,50+1):
     tickets_sold=tickets_sold+1
print("Sold out:", tickets_sold, "tickets sold!")
SyntaxError: invalid syntax

print("Sold out:", tickets_sold, "tickets sold!")
Sold out: 0 tickets sold!


tickets_sold=0
max_capacity=50
for i in range(1,50+1):
     tickets_sold=tickets_sold+1
     
SyntaxError: multiple statements found while compiling a single statement


tickets_sold=0
max_capacity=50
for i in range(1,50+1):
    tickets_sold=tickets_sold+1
print("Sold out:", tickets_sold, "tickets sold!")
SyntaxError: invalid syntax

tickets_sold=0
max_capacity=50
for i in range(1,50+1):
    
SyntaxError: multiple statements found while compiling a single statement


tickets_sold=0
max_capacity=50
for i in range(1,50+1):
  tickets_sold=tickets_sold+1
print("sold out:",tickets_sold,"tickets sold")
SyntaxError: invalid syntax
tickets_sold=0
max_capacity=50
for i in range(1,50+1):
  tickets_sold=tickets_sold+1
print("sold out:",tickets_sold,"tickets sold")
SyntaxError: invalid syntax
tickets_sold=0
max_capacity=50
for tickets in range(1, max_capacity + 1):
    tickets_sold +=1
print("sold out",tickets_sold,"tickets sold")
SyntaxError: invalid syntax
tickets_sold=0
max_capacity=50
for i in range(1,50+1):
    tickets_sold=tickets_sold+1

    
print("sold out",tickets_sold,"tickets sold")
sold out 50 tickets sold
##########################

#####conditional loop with dictionary
courses={"LLM concepts":"AI","Introduction to Data Pipelines":"Data Engineering","AI Ethics":"AI","Introduction to dbt":"data engineering","Writing Efficient Python Code": "Programming","Introduction to Docker": "Programming"}
type(courses)
<class 'dict'>
for key, value in courses.items()
SyntaxError: expected ':'
for key, value in courses.items():
    if value == "AI":
        print(key,"is an AI Course")## checks if the value is AI

        
LLM concepts is an AI Course
AI Ethics is an AI Course
for key, value in courses.items():
    if value == "AI":
        print(key,"is an AI course")
elif value == "Programming":
    
SyntaxError: invalid syntax
for key, value in courses.items():
    if value == "AI":
        print(key,"is an AI Course")## checks if the value is AI

        
LLM concepts is an AI Course
AI Ethics is an AI Course
elif value == "Programming":
    
SyntaxError: invalid syntax

======= RESTART: D:/sample projects/python_sample_programs/for_working.py ======
Traceback (most recent call last):
  File "D:/sample projects/python_sample_programs/for_working.py", line 2, in <module>
    for key, value in courses.items():
NameError: name 'courses' is not defined

======= RESTART: D:/sample projects/python_sample_programs/for_working.py ======
LLM concepts is an AI course
Introduction to Data Pipelines is a Data Engineering course
AI Ethics is an AI course
Introduction to dbt is a Data Engineering course
Writing Efficient Python Code is a Programming course
Introduction to Docker is a Programming course

= RESTART: D:/sample projects/python_sample_programs/conditional_loop_with_dic.py
LLM concepts is an AI course
Introduction to Data Pipelines is a Data Engineering course
AI Ethics is an AI course
Introduction to dbt is a Data Engineering course
Writing Efficient Python Code is a Programming course
Introduction to Docker is a Programming course
courses={"LLM concepts":"AI","Introduction to Data Pipelines":"Data Engineering","AI Ethics":"AI","Introduction to dbt":"data engineering","Writing Efficient Python Code": "Programming","Introduction to Docker": "Programming"}


### while loop

stock=10
num_purchases=0
while num_purchases < stock:
    num_purchases+=1
    print(stock - num_purchases)

    
9
8
7
6
5
4
3
2
1
0

= RESTART: D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py
Traceback (most recent call last):
  File "D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py", line 3, in <module>
    while num_purchases < stock:
NameError: name 'num_purchases' is not defined. Did you mean: 'num_of_purchases'?

= RESTART: D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py
Traceback (most recent call last):
  File "D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py", line 3, in <module>
    while num_purchases < stock:
NameError: name 'num_purchases' is not defined. Did you mean: 'num_of_purchases'?

= RESTART: D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py
Plenty of stock remaining
Plenty of stock remaining
some stock remaining
some stock remaining
some stock remaining
some stock remaining
Low stock!
Low stock!
Low stock!
No stock!



tickets_sold = 0
max_capacity = 50
while ticket_sold < max_capacity:
    tickets_sold+=1
print("sold out:",tickets_sold,"tickets sold")
SyntaxError: invalid syntax
print("sold out:",tickets_sold,"tickets sold")
sold out: 0 tickets sold

= RESTART: D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py
Plenty of stock remaining
Plenty of stock remaining
some stock remaining
some stock remaining
some stock remaining
some stock remaining
Low stock!
Low stock!
Low stock!
No stock!
Traceback (most recent call last):
  File "D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py", line 20, in <module>
    while ticket_sold < max_capacity:
NameError: name 'ticket_sold' is not defined. Did you mean: 'tickets_sold'?
while ticket_sold < max_capacity:
    tickets_sold+=1

    
Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    while ticket_sold < max_capacity:
NameError: name 'ticket_sold' is not defined. Did you mean: 'tickets_sold'?
tickets_sold = 0
max_capacity = 50
while ticket_sold < max_capacity:
    tickets_sold+=1

    
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    while ticket_sold < max_capacity:
NameError: name 'ticket_sold' is not defined. Did you mean: 'tickets_sold'?
while tickets_sold < max_capacity:
    tickets_sold+=1

    
print("sold out:",tickets_sold,"tickets sold")
sold out: 50 tickets sold



= RESTART: D:/sample projects/python_sample_programs/conditional_statement_within_whileloop.py
Plenty of stock remaining
Plenty of stock remaining
some stock remaining
some stock remaining
some stock remaining
some stock remaining
Low stock!
Low stock!
Low stock!
No stock!
sold out: 50 tickets sold

= RESTART: D:/sample projects/python_sample_programs/conditional_while_loop.py =
Coming soon
Coming soon
Purchase b4 21st for early access
Coming soon
Coming soon
Coming soon
Coming soon
Available now!
Available now!
Available now!
Available now!

= RESTART: D:/sample projects/python_sample_programs/conditional_while_loop.py =
Purchase b4 21st for early access
Purchase b4 21st for early access
Coming soon
Coming soon
Coming soon
Coming soon
Coming soon
Available now!
Available now!
Available now!
Available now!



#### the "not" keyword
print(products_dict)
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    print(products_dict)
NameError: name 'products_dict' is not defined
product_dict
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    product_dict
NameError: name 'product_dict' is not defined
products_dict = {"AG32":10,"HT91":20,"PL65":30,"OS31":15,"KB07":25,"TR48":35}
print(products_dict)
{'AG32': 10, 'HT91': 20, 'PL65': 30, 'OS31': 15, 'KB07': 25, 'TR48': 35}
if "0S31" not in products_dict.keys:
    print(False)
else:
    print(True)

    
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    if "0S31" not in products_dict.keys:
TypeError: argument of type 'builtin_function_or_method' is not iterable
if "0S31" not in products_dict.keys():
    print(False)
else:
    print(True)

    
False
### the "and" keyword
if "HT91" in products_dict.keys() and min(products_dict.values()) > 5:
    print(True)
else
SyntaxError: expected ':'
else:
    
SyntaxError: invalid syntax
if "HT91" in products_dict.keys() and min(products_dict.values()) > 5:
    print(True)
else:
    print(False)

    
True
#### "or keyword"

if "HT91" in products_dict.keys() or min(products_dict.values()) > 5:
    print(True)
else:
    print(False)

    
True


####  appending
####   store information that meets specific criteria in a list

expensive_products=[]
## empty list

for key,val in products_dict.items():
    if val >= 20:
        expensive_products.append(key)

        
print(expensive_products)
['HT91', 'PL65', 'KB07', 'TR48']


authors={"Nicholas Sparks":30 "Judith Krantz":20, "Harold Robbins":25, "J. K. Rowling":55, "Sidney Sheldon":23}
SyntaxError: invalid syntax. Perhaps you forgot a comma?
authors={"Nicholas Sparks":30,"Judith Krantz":20, "Harold Robbins":25, "J. K. Rowling":55, "Sidney Sheldon":23}
authors_below_22=[]
for key,value in authors.items():
    if value < 22:#check for values less than 22
        authors_below_22.append(key)
        ### appending authors to list

        
print(authors_below_22)
['Judith Krantz']

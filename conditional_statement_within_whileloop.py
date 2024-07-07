stock=10
num_of_purchases=0
while num_of_purchases < stock:
    num_of_purchases+=1#increment num purchases
    if stock - num_of_purchases > 7:
        print("Plenty of stock remaining")
    elif stock - num_of_purchases > 3:
        print("some stock remaining")
    elif stock - num_of_purchases != 0:
        print("Low stock!")
    else:
        print("No stock!")
        
    
#####while loop example


tickets_sold = 0
max_capacity = 50
while tickets_sold < max_capacity:
    tickets_sold+=1


print("sold out:",tickets_sold,"tickets sold")        

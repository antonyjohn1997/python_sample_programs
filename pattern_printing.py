def pyramid(n):
    for i in range(1,n+1):
        #for j in range(n-i):#print spaces
            #print("",end="")
        for k in range(1,2*i):
            print("*",end="")
        print()#move to next line        


rows=int(input("Enter the number of rows:"))
pyramid(rows)
    
    

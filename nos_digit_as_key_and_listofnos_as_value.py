#def fibonacci():
    #{
        #fibs=[]
       # a,b =0,1
       # while number > 0 :
          #  fibs.append(a)
          #  a,b=b,a+b
          #  n-=1
       # return fibs    
       # }

    
    
#number=10
#print(fibonacci)

       #===================

       
#ss = "Nory was a Catholic because her mother was a Catholic, and Nory's mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been."

#words = ss.split()
#d= {x:0 for x in words}

#for w in words:
 # d[w]+=1
#print(d.items())
#type(d.items)
#ds = sorted(d.items(), key=lambda x:x[1], reverse=True) 


#=============


#cities = {'San Francisco': 'US', 'London':'UK',
        #'Manchester':'UK', 'Paris':'France',
        #'Los Angeles':'US', 'Seoul':'Korea' }


#ds={}
#for city,country in cities.items():
    #if country not in ds:
      #  ds[country]=[]
      #  print(ds[country])
    #ds[country].append(city)
#print(ds)



      #==================


#a=[3,4,6,10,11,18]
#b=[1,5,7,12,13,19,21]
#c=[]
#i,j=0,0
#while i<len(a) and j<len(b):
    #if a[i]<b[j]:
       # c.append(a[i])
       # i+=1
    #else:
     #   c.append(b[j])
     #   j+=1
#while i<len(a):
  #  c.append(a[i])
   # i+=1
#while j<len(b):
    #c.append(b[j])
   # j+=1
#print(c)

  # ==================


L=[1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]
d={}
for i in L:
    num_digits=len(str(i))
    #print(num_digits)
    if num_digits not in d:
        d[num_digits]=[]
        print(d)
    d[num_digits].append(i)
print(d)    
    
        
    

#def raising_python_exception(x,y):
    #try:
        #z=x/y
    #except zerodivisionerror,e:
        #err=e
    #print e
#raising_python_exception(1,2)    
def divide(x,y):
    if y==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y
try:
    result = divide(10,0)
except ZeroDivisionError as e:
    print(f"Error: {e}")

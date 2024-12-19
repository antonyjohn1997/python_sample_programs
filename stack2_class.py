class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
        return len(self.stack)
        
    def __str__(self):
        return f"stack({self.stack})"    
                    

    
stack=Stack() 
stack.push(10)
stack.push(20)
stack.push(30)

print("stack after pushes:",stack.stack)
print("top item: ",stack.peek())
popped_item= stack.pop()
print("popped item:",popped_item)
print("stack after pop:",stack.stack)

print("Is stack empty?",stack.is_empty())

print("stack size:",stack.size())

stack.pop()
stack.pop()
print("stack after popping all items:", stack.stack)

## try popping from an empty stack

try:
    stack.pop()
except IndexError as e:
    print("Error:",e)    
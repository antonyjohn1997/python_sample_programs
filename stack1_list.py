stack=[]

## push
stack.append(1)
stack.append(2)
stack.append(3)

print("stack after pushing:",stack)

##pop
top=stack.pop()
print("popped element:",top)
print("stack after pop operation:", stack)

## peek
top=stack[-1]
print("top elememt:",top)

## check if stack is empty
is_empty=len(stack)==0
print("Is the stack is empty?",is_empty)
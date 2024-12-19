queue=[]
def enqueue(queue,item):
    queue.append(item)
def dequeue(queue):
    if not is_empty(queue):
        return queue.pop(0)
    else:
        return "queue is empty" 
def front(queue):
    if not is_empty(queue):
        return queue[0]
    else:
        return "queue is empty"
def rear(queue):
    if not is_empty(queue):
        return queue[-1] 
    else:
        return "queue is empty"          
def is_empty(queue):
    if not size(queue):
       return len(queue)==0

def size(queue):
    return len(queue)            
enqueue(queue,10)  
enqueue(queue,20)
enqueue(queue,30)

print("after inserting element the queue is :",queue)
print("front is :",front(queue))
print("rear is:",rear(queue))
print("dequed item",dequeue(queue))
print("after deleting item the queue is :",queue)
print("front is :",front(queue))
print("rear is:",rear(queue))
print("size of queue",size(queue))
print("is the queue empty?",is_empty(queue))
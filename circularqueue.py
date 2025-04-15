size = 5
queue = [None] * size  
front = -1
rear = -1

def enqueue(value):
    global front, rear
    if (rear + 1) % size == front:
        print("Queue is Full!")
        return
    
    if front == -1:  
        front = 0
    rear = (rear + 1) % size
    queue[rear] = value
    print("Enqueued:", value)
    print("Queue:", queue)

def dequeue():
    global front, rear
    if front == -1:  
        print("Queue is Empty!")
        return None
    
    dequeued_value = queue[front]
    
    queue[front] = None
    
    if front == rear:  
        front = rear = -1
    else:
        front = (front + 1) % size
    
    print(f"Dequeued: {dequeued_value}")
    print("Queue:", queue)
    return dequeued_value


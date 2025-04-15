# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)

# print(queue[0])

# print(not queue)


# queue = []

# queue.append(("Normal Patient",2))
# queue.append(("Critical Patient",1))
# queue.append(("Check-up Patient",3))

# print(queue)

# queue.sort(key = lambda x:x[1])

# print(queue) 

# person,priority = queue.pop(0)
# print(f"Serving: {person}")  
# print(queue)


# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)
# queue.pop(0)
# print(queue)
# queue.append(40)
# print(queue)
# queue.insert(0,10)
# print(queue)
# queue.pop()
# print(queue)

# word = "madsam"
# queue = list(word)
# print(queue)
# ispalindrome = True
# while len(queue)>1:
#     front = queue.pop(0)
#     rear = queue.pop()

#     if front != rear:
#         ispalindrome = False
#         break

# if ispalindrome:
#     print(f"{word} is pallindrome")
# else:
#     print(f"{word} is not pallindrome")


size = 5
queue = [None] * size
front = -1
rear = -1

if (rear + 1) % size != front:
    rear = (rear + 1) % size
    queue[rear] = 10
    if front == -1:
        front = rear
print(queue)

if (rear + 1) % size != front:
    rear = (rear + 1) % size
    queue[rear] = 20
print(queue)

if front != -1:
    print("Dequeued:", queue[front])
    queue[front] = None
    if front == rear:
        front = rear = -1
    else:
        front = (front + 1) % size
print(queue)






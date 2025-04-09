class Stack:
    def __init__(self):
        self.stack =[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.stack.pop()
    def peek(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.stack[-1]

    def isempty(self):
        return len(self.stack)==0
    
    def display(self):
        if self.isempty():
            return "stack is empty"
        else:
            return self.stack

s = Stack()

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Is Empty")
    print("5. Display")
    print("6. Exit")
    
    select = int(input("Select your operation (1-6): "))

    if select == 1:
        data = int(input("Enter value to push: "))
        s.push(data)
    elif select == 2:
        print("Popped element:", s.pop())
    elif select == 3:
        print("Top element:", s.peek())
    elif select == 4:
        print("Is stack empty?", s.isempty())
    elif select == 5:
        print("stack elements:",s.display())
    elif select == 6:
        print("Exiting...")
        break
    else:
        print("Invalid selection, please try again.")



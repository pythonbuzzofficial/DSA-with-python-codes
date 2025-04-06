class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head
        self.head = new_node

    # Insert after a specific node
    def insert_after(self, target, data):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Target node not found")

    # Insert before a specific node
    def insert_before(self, target, data):
        if not self.head:
            print("List is empty")
            return

        prev = None
        curr = self.head

        while True:
            if curr.data == target:
                new_node = Node(data)
                if prev is None:
                    # Insert before head
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = new_node
                    new_node.next = self.head
                    self.head = new_node
                else:
                    prev.next = new_node
                    new_node.next = curr
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break
        print("Target node not found")

    # Delete at end
    def delete_end(self):
        if not self.head:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

    # Delete at beginning
    def delete_beginning(self):
        if not self.head:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        last.next = self.head.next
        self.head = self.head.next

    # Delete by value
    def delete_by_value(self, value):
        if not self.head:
            print("List is empty")
            return

        curr = self.head
        prev = None

        while True:
            if curr.data == value:
                if prev is None:
                    # Deleting head
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        temp.next = self.head.next
                        self.head = self.head.next
                else:
                    prev.next = curr.next
                return
            prev = curr
            curr = curr.next
            if curr == self.head:
                break
        print("Value not found")

    # Traversal
    def display(self):
        if not self.head:
            print("List is empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

# Example usage:
cll = CircularLinkedList()
cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.display()

cll.insert_beginning(5)
cll.display()

cll.insert_after(20, 25)
cll.display()

cll.insert_before(10, 7)
cll.display()

cll.delete_beginning()
cll.display()

cll.delete_end()
cll.display()

cll.delete_by_value(25)
cll.display()

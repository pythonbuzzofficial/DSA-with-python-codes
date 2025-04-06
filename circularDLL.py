class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        last = self.head.prev
        last.next = new_node
        new_node.prev = last
        new_node.next = self.head
        self.head.prev = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return
        last = self.head.prev
        new_node.next = self.head
        new_node.prev = last
        self.head.prev = new_node
        last.next = new_node
        self.head = new_node

    def insert_after(self, target_data, new_data):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            if temp.data == target_data:
                new_node = Node(new_data)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Target node not found")

    def insert_before(self, target_data, new_data):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            if temp.data == target_data:
                new_node = Node(new_data)
                new_node.prev = temp.prev
                new_node.next = temp
                temp.prev.next = new_node
                temp.prev = new_node
                if temp == self.head:
                    self.head = new_node
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Target node not found")

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
            return
        last = self.head.prev
        self.head = self.head.next
        self.head.prev = last
        last.next = self.head

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if self.head.next == self.head:  # Only one node
            self.head = None
            return
        last = self.head.prev
        second_last = last.prev
        second_last.next = self.head
        self.head.prev = second_last

    def delete_by_value(self, target_data):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            if temp.data == target_data:
                if temp.next == temp:  # Only one node
                    self.head = None
                    return
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next
            if temp == self.head:
                break
        print("Node not found")

    def traverse_forward(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("HEAD")

# Usage Example
dll = DoublyCircularLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_beginning(5)
dll.insert_after(10, 15)
dll.insert_before(20, 18)
dll.traverse_forward()

dll.delete_at_beginning()
dll.delete_at_end()
dll.delete_by_value(15)
dll.traverse_forward()

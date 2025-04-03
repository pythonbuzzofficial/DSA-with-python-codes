class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def traverse_forward(self):
        if self.head is None:
            print("DLL is empty.")
            return
        temp= self.head
        while temp:
            print(temp.data,end="<->")
            temp = temp.next
        print("None")
        
    def traverse_backward(self):
        if self.head is None:
            print("DLL is empty.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data,end="<->")
            temp = temp.prev
        print("None")
    
      
    def insert_after(self,target_data,new_data):
        temp = self.head
        while temp and temp.data != target_data:
            temp = temp.next
        
        if not temp:
            print("target node not found")
            return

        new_node = Node(new_data)

        new_node.next = temp.next
        new_node.prev = temp
        
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def insert_before(self,target_data,new_data):
        temp = self.head
        while temp and temp.data != target_data:
            temp = temp.next
        
        if not temp:
            print("target node not found")
            return

        new_node = Node(new_data)

        new_node.next = temp
        new_node.prev = temp.prev
        temp.prev.next = new_node
        temp.prev = new_node
    
    def delete_at_beginning(self):
        if self.head is None:
            print("DLL is empty.")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None
    
    def delete_at_end(self):
        if self.head is None:
            print("DLL is empty.")
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        if temp.prev:
            
            temp.prev.next = None
        else:
            self.head = None

    def delete_by_value(self,target_data):
        if self.head is None:
            print("DLL is empty.")
            return
        temp = self.head
        while temp and temp.data!= target_data:
            temp = temp.next
        if not temp:
            print("target data not found.")
            return
        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next
                
        if temp.next:
            temp.next.prev = temp.prev

        

   
DLL = DoublyLinkedList()
DLL.insert_at_end(10)
DLL.insert_at_end(20)
DLL.insert_at_end(30)
DLL.traverse_forward()
DLL.delete_by_value(20)
DLL.traverse_forward()








        

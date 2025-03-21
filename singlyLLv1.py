class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
       
    def insert_at_beginning(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head=new_node
    
    def insert_at_end(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next= new_node   
        
    def traverser(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data,end=" --> ")
            temp = temp.next
        print("None")
    def insert_after(self,target_data,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head =new_node
            return
        temp = self.head
        while temp.data!= target_data:
            temp =  temp.next
            
        new_node.next =temp.next
        temp.next =new_node        
    def insert_before(self,target_data,new_data):
        if self.head is None:
             print("Linked list is empty")
             return
        new_node = Node(new_data)
        if self.head.data == target_data:
             new_node.next = self.head
             self.head = new_node
             return
         
        temp = self.head
        while temp.next.data != target_data:
            temp = temp.next
            
        new_node.next = temp.next
        temp.next = new_node
    def delete_at_beginning(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next   
    def delete_at_end(self):
        if self.head is None:
            print("Linked list is empty")
            return   
        if self.head.next is None:
            self.head=None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None 
    def delete_by_value(self,target_data):
        if self.head is None:
            print("Linked list is empty")
            return  
        if self.head.data == target_data:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next.data != target_data:
            temp = temp.next
            if temp.next is None:
                print("node not found")
                return            
        temp.next = temp.next.next        
        

               
    
LL = LinkedList()
LL.insert_at_end(10)
LL.insert_at_end(20)
LL.insert_at_end(30)
LL.traverser()
LL.delete_by_value(60)
LL.traverser()










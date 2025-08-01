from singly_linked_list import *
class Stack:
    def __init__(self):
        self.my_list=SLL()
        self.item_count=0
        
    def is_empty(self):
        return self.my_list.is_empty==None
    
    def push(self,data):
        self.my_list.insert_at_beginning(data)
        self.item_count+=1
        
    def pop(self):
        if not self.is_empty:
            self.my_list.delete_first()
            self.item_count-=1
            
    def peek(self):
        if not self.is_empty():
            return self.my_list.start.item
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return self.item_count
    
    def print_stack(self):
        if not self.is_empty():
            temp=self.my_list.start
            while temp!=None:
                print (temp.item)
                temp=temp.next
            
        else:
            print("stack is empty")
    
    
s=Stack()
s.push(100)
s.push(200)
s.push(300)
print("popped element:",s.pop())
print("Top element:",s.peek())
s.print_stack()
     
            
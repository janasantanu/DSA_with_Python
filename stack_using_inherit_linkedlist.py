from singly_linked_list import *
class Stack(SLL):
    def __init__(self):
        self.item_count=0
        super().__init__()
    def is_empty__(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_beginning(data)
        self.item_count+=1
    def pop(self):
        
        if self.is_empty():
            
            raise IndexError("stack underflow")
        else:
            pop_element=self.start.item
            self.delete_first()
            self.item_count-=1
            return pop_element
            
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("stack underflow")
        
    def size(self):
        return self.item_count
    
    def print_stack(self):
        if not self.is_empty():
            temp=self.start
            while temp!=None:
                print(temp.item)
                temp=temp.next
        else:
            raise IndexError("stack is underflow")
                
                
    
s=Stack()
s.push(10)
s.push(20)
s.push(40)
s.push(70)
print("pop element:",s.pop())
print("top element:",s.peek())
s.print_stack()    

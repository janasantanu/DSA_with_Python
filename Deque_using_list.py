class Deque:
    def __init__(self):
        self.my_list=[]
       
    def is_empty(self):
        return len(self.my_list)==0
    
    
    def insert_front(self,data):
        self.my_list.insert(0,data)
        
    def insert_rear(self,data):
        self.my_list.append(data)
        
    def delete_front(self):
        if not self.is_empty():
            self.my_list.pop(0)
        else:
            raise IndexError("Deque is empty")
        
    def delete_rear(self):
        if not self.is_empty():
            self.my_list.pop(-1)
        else:
            raise IndexError("deque is empty")
        
    def get_front(self):
        if not self.is_empty():
            return self.my_list[0]
        else:
            raise IndexError("Deque is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.my_list[-1]
        else:
            raise IndexError("deque is empty")
        
    def size(self):
        return len(self.my_list)
    
    def print_element(self):
        if not self.is_empty():
            print(self.my_list)
            
D=Deque()
D.insert_front(10)
D.insert_rear(20)
D.insert_front(30)
D.insert_rear(40)
D.delete_front()
D.delete_rear()
print(D.get_front(),D.get_rear())
D.print_element()
print(D.size())      
        
    
class Node:  
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DCLL:
    def __init__(self, start=None):  
        self.start = start
    
    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self, data):
        N = Node(data)  
        if not self.is_empty():  
            N.next = self.start
            N.prev = self.start.prev
            self.start.prev.next = N
            self.start.prev = N
        else:
            N.next = N
            N.prev = N
        self.start = N
        
    def insert_at_last(self, data):
        N = Node(data) 
        if not self.is_empty():  
            N.prev = self.start.prev
            N.next = self.start
            self.start.prev.next = N
            self.start.prev = N
        else:
            N.next = N
            N.prev = N
            self.start = N
            
    def search(self, data):
        temp = self.start
        if self.start == None:
            return None
        if temp.data == data:
            return temp
        temp = temp.next
        while temp != self.start:
            if temp.data == data:
                return temp
            temp = temp.next
        return None
            
    def insert_after(self, temp, data):
        if temp != None:
            N = Node(data)  
            N.next = temp.next
            N.prev = temp
            temp.next.prev = N
            temp.next = N  
            
    def print_list(self):
        temp = self.start
        if temp != None:
            print(temp.data, end=' ')
            temp = temp.next
            while temp != self.start:
                print(temp.data, end=' ')
                temp = temp.next
        print()  
                
    def delete_first(self):
        if self.start != None:
            if self.start.next == self.start:
                self.start = None  
            else:
                self.start.prev.next = self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next
                
    def delete_last(self):
        if self.start != None:
            if self.start.next == self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
                
    def delete_item(self, data):
        if self.start != None:
            temp = self.start
            if temp.data == data:
                self.delete_first()
            else:
                temp = temp.next
                while temp != self.start:
                    if temp.data == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                        break


my_list = DCLL()  
my_list.insert_at_start(40)
my_list.insert_at_start(50)
my_list.insert_at_last(70)
my_list.delete_first()
my_list.insert_after(my_list.search(50), 700)
my_list.print_list()

                    
                    
                
        
                
                
        
        
            
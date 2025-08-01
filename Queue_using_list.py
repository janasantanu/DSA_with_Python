class Queue:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    
    def enqueue(self,data):
        return self.item.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        else:
            raise IndexError("queue is empty")
        
    def get_front(self):
        if not self.is_empty():
            
            return self.item[0]
        else:
            raise IndexError("queue is underflow")
            
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("queue is underflow")
        
    def size(self):
        return len(self.item)
    
Q=Queue()
#print(Q.get_front()) #this line will throw an Attribute error msg 
#exceptional handling
try:
    print(Q.get_front())
except IndexError as e:
    print (e.args[0])
    
Q.enqueue(100)
Q.enqueue(200)
Q.enqueue(300)
Q.dequeue()
Q.size()
print(Q.item)

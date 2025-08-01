class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0
        
    def is_empty(self):
        return self.item_count==0
    
    def enqueue(self,data):
        n=Node(data)
        if not self.is_empty():
            self.rear.next=n
            self.rear=n
        else:
            self.front=n
            self.rear=n
        self.item_count+=1
        
    def dequeue(self):
        if not self.is_empty():
            self.front=self.front.next
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            raise IndexError("Queue is empty")
        self.item_count-=1
        
    def get_front(self):
        if  not self. is_empty():
            return self.front.data
        else:
            raise IndexError("queue is empty")
        
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        else:
            raise IndexError("queue is empty")
            
    def size(self):
        return self.item_count()
    
    def print_element(self):
        if not self.is_empty():
            temp=self.front
            while temp!=None:
                print (temp.data)
                temp=temp.next
        
    
Q=Queue()
Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.dequeue()
Q.enqueue(100)
print("front element is: ",Q.get_front())
Q.print_element()


        
    
        
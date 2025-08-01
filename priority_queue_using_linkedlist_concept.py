class Node:
    def __init__(self,data=None,priority=None,next=None):
        self.data=data
        self.priority=priority
        self.next=next
        
class Priority_queue:
    def __init__(self,start=None):
        self.start=start
        self.item_count=0
        
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start or priority<self.start.priority:
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while temp.next and temp.next.priority<=priority:
                temp=temp.next
            n.next=temp.next
            temp.next=n
        self.item_count+=1
        
    def is_empty(self):
        return self.start==None
    
    def pop(self):
        if self.is_empty():
            raise IndexError("empty")
        else:
            data=self.start.data
            self.start=self.start.next
            return data
        self.item_count-=1
        
    def size(self):
        return self.item_count
    
p=Priority_queue()
p.push("amit",1)
p.push("sanu",2)
p.push(3,5)
while not p.is_empty():
    print (p.pop())
            
            
        
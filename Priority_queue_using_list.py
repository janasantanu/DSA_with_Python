class priorityQueue:
    def __init__(self):
        self.my_list=[]
    
    def push(self,data,priority):
        index=0
        while index<len(self.my_list)and self.my_list[index][1]<=priority:
            index+=1
        self.my_list.insert(index,(data,priority))
        
    def is_empty(self):
        return len (self.my_list)==0
    
    def pop(self):
        if not self.is_empty():
            return self.my_list.pop(0)[0]
        else:
            raise IndexError("empty")
        
    def size(self):
        return len (self.my_list)
        
        
p=priorityQueue()
p.push(100,2)
p.push(200,3)
p.push(300,1)
p.push("sanu",5)
while not p.is_empty():
    print(p.pop())
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if not self.is_empty():
            return(self.items[-1])
        else:
            raise IndexError("stack is empty")
    
    def size(self):
        return len(self.items)
    
s=Stack()
s.push(100)
s.push(50)
s.push(25)

print(s.pop())
s.push(100)
print("Top Element = ",s.peek())
print(s.items)         
        
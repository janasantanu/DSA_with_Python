

#inherit from inbuild class list
class Stack(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        self.append(data)
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    def size(self):
        return len(self)
    ## not to inherit insert() from parent class list
    def insert(self,index,data):
        raise AttributeError("invalid attribute")
    
s=Stack()
s.push(100)
s.push(200)
s.push(300)
s.pop()
s.pop()
s.push(500)
print("top value",s.peek())
s.push(1000)
#s.insert(2,6000)
print(s)
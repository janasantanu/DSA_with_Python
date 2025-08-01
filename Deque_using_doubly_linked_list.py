class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0
    
    def is_empty(self):
        return self.item_count == 0
    
    def insert_front(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            n.next = self.front
            self.front.prev = n
            self.front = n
        self.item_count += 1
    
    def insert_at_rear(self, data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            n.prev = self.rear
            self.rear.next = n
            self.rear = n
        self.item_count += 1
    
    def delete_front(self):
        if self.is_empty():
            raise IndexError("empty deque")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.item_count -= 1
    
    def delete_rear(self):
        if self.is_empty():
            raise IndexError("empty deque")
        elif self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.item_count -= 1
    
    def get_front(self):
        if not self.is_empty():
            return self.front.data
        raise IndexError("empty deque")
    
    def get_rear(self):
        if not self.is_empty():
            return self.rear.data
        raise IndexError("empty deque")
    
    def size(self):
        return self.item_count
    
    def print(self):
        temp = self.front
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next
        


D = Deque()
D.insert_front(100)
D.insert_front(200)
D.insert_at_rear(300)
D.insert_at_rear(500)
print("Front:", D.get_front(), "Rear:", D.get_rear())
D.print()
    
            
            
            
            
            
            
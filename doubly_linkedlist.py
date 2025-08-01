class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
    def __init__(self):
        self.start = None
    
    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        if self.start is None:
            self.start = Node(None, data, None)
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            n = Node(temp, data, None)
            temp.next = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def del_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def del_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None

    def del_item(self, data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.data == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next



my_list = DLL()
my_list.insert_at_start(25)
my_list.insert_at_last(100)
my_list.insert_after(my_list.search(25), 5000)
my_list.print_list()  

        
                                
        
            
    
    
    
        
        

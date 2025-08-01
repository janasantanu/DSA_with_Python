class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_beginning(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

    def insert_after_searched_value(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp = temp.next
        print()
        
    def delete_first(self):
        if not self.is_empty():
            self.start=self.start.next
            
    def delete_last(self):
        if not self.is_empty():
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
        else:
            self.start=None
            
    def delete_item(self,data):
        if self.start==None:
            pass
        elif self.start.next==None:
            if self.start.item==data:
                self.start=None
        else:
            temp=self.start
            if temp.item==data:
                self.start=temp.next
            else:
                while temp.next!=None:
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next
                    
        
T=int(input("enter no: "))

my_list = SLL()
my_list.insert_at_beginning(T)
my_list.insert_at_last(100)
my_list.print_list()  
        
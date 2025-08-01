class node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class cll:
    def __init__(self,last=None):
        self.last=last
        
    def is_empty(self):
        return self.last==None
    
    def insert_at_first(self,data):
        n=node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
        
    def insert_at_last(self,data):
        n=node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
            
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    
    def insert_after(self,temp,data):
        if temp!=None:
            n=node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
    def print_list(self):
        if not self.is_empty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item)
            
##deletion
    def delete_at_first(self):
        if not is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next,next
                
    def delete_at_last(self):
        if not is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                if temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
                else:
                    if self.last.next==data:
                        self.delete_at_first()
            else:
                temp=self.last.next
            while temp!=self.last:
                if temp.next==self.last:
                    if self.last.item==data:
                        self.delete_at_last()
                        break
                    if temp.next.item==data:
                        temp.next=temp.next.next
                        break
                    temp=temp.next

cir = cll()
cir.insert_at_first(10)
cir.insert_at_first(20)
cir.insert_at_last(30)
cir.insert_at_last(40)
cir.insert_after(cir.search(10), 600)
cir.print_list()
                    
        
                
                        
        
                
                
        
        
            
            
        
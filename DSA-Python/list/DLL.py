class Node:
    def __init__(self,prev=None,next=None,item=None):
         self.prev=prev
         self.item=item      
         self.next=next
class SLL:
    def __init__(self,start=None):
        self.start=start
        self.end=start.next
    def is_Empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_Empty():
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:            
          while temp.next!=None:
           temp=temp.next

        n=Node(temp,data,None)
        if temp==None:
            self.start=n
        else:
            temp.next=n

    def search(self,data):
        
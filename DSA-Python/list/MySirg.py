"""Single linked list"""

class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
class SLL:
    def __init__(self,start=None):
           self.start=start
    def is_Empty(self):
         return self.start==None
    def insertAtStart(self,data):
         n=Node(data,self.start)
         self.start=n
    def insertAtLast(self,data):
         n=Node(data)
         if not self.is_Empty:
              temp=self.start
              while temp.next is not None:
                   temp=temp.next
              temp.next=n
         else:
              self.start=n
                       
                   
              


mysll=SLL()
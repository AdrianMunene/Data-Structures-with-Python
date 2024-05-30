#Attempt to implement class TreeNode() to accept arguments when creating an object/instance
class Node():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, data=0, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def head(self):
        if self.previous == None:
            return True
        return False
    
    def tail(self):
        if self.next == None:
            return True
        return False
    

def sortList(head):
    if head == None or head.next == None:
        return head
    if head.data < head.next.data:
        sortList(head.next)
        return head 
    else:
        head.next = sortList(head.next)


a1 = Node(data = 34)
a2 = Node(data = 20)
a3 = Node(data = 35)
a4 = Node(data = 68)

a1.next = a2
a2.previous = a1
a2.next = a3
a3.previous = a2
a3.next = a4
a4.previous = a3


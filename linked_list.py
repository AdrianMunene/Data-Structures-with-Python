#doubly linked list
#Attempt to implement class TreeNode() to accept arguments when creating an object/instance
class Node():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, data=0, next=None): #previous=None
        self.data = data
        self.next = next
        #self.previous = previous


#reversed linked list
def reverseList(head):
    if head == None or head.next == None:
        return head
    p = reverseList(head.next)
    head.next.next = head
    head.next = None
    return p

a1 = Node()
a2 = Node()
a3 = Node()
a4 = Node()
a1.data = 34
a1.next = a2
a2.data = 20
a2.next = a3
a3.data = 35
a3.next = a4
a4.data = 68

reverseList(a1)


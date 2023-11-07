class Node:
    def __innit__(self, data, next=None ):
        self.data = data
        self.next = next

a1 = Node()
a2 = Node()
a1.data = [32, 34]
a1.next = a2
a2.data = {'Adrian':20}

print(a1.next.data)
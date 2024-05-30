'''The Deque is the only Python data structure with fast Queue operations. (Note queue.Queue isn't normally suitable,
since it's meant for communication between threads.) A basic use case of a Queue is the breadth first search.'''
from collections import deque
#from pprint import pprint
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def breadthfirstsearch(root):
    #A dictionary that shows all the nodes that can be visited from a particular node
    tree = {}

    if root is None:
        return 
    
    queue = deque([root])

    while queue:
        #popleft is dequeue, cause queue operates on FIFO and we want element at index 0
        current = queue.popleft()

        tree[current.val] = []

        if current.left != None:
            queue.append(current.left)
            tree[current.val].append(current.left.val)

        if current.right != None:
            queue.append(current.right) 
            tree[current.val].append(current.right.val)
#delete entries in tree {} with no child nodes
    for i in list(tree.keys()):
        if tree[i] == []:
            del tree[i]

    return tree
        


root = TreeNode()
a1 = TreeNode()
a2 = TreeNode()
a3 = TreeNode()
a4 = TreeNode()
a5 = TreeNode()
a6 = TreeNode()
a7 = TreeNode()
a8 = TreeNode()

root.val = 0
a1.val = 5
a2.val = 2
a3.val = 7
a4.val = 9
a5.val = 4
a6.val = 12
a7.val = 256
a8.val = -99

root.left = a1
root.right = a2
a1.left = a3
a1.right = a5
a2.left = a6
a2.right = a4
a5.left = a7
a6.right = a8

breadthfirstsearch(root)

# def breadthfirstsearch(graph, root):
#     distances = {}
#     distances[root] = 0
#     #Iterable passed as an argument to deque
#     q = deque([root])
#     while q:
#         #The oldest seen (but not yet visited) node will be the left most one
#         current = q.popleft()
#         print(current)
#         for neighbour in graph[current]:
#             if neighbour not in distances:
#                 distances[neighbour] = distances[current] + 1
#                 print(distances)
#                 q.append(neighbour)
#                 print(q)
#     return distances


# graph = {1:[2,3], 2:[4], 3:[4,5], 4:[3,5], 5:[]}

# print(breadthfirstsearch(graph, 1))


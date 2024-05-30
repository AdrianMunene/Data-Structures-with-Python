class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


"""This function inserts a node into an already existing binary tree
If root is passed as None, it creates a new tree"""
def insertNode(root, val):
    if root == None:
        root = TreeNode()
        root.val = val
        return root
    
    if root.val < val:
        root.right = insertNode(root.right, val)
    else:
        root.left = insertNode(root.left, val)

    return root

#Building a BST by inserting into a blank binary search tree
#when we create the bst this way, a becomes the root node that identfies the binary search tree
a = insertNode(None, 156)
b = insertNode(a, 23)
c = insertNode(a, 45)
d = insertNode(a, 625)
e = insertNode(a, 566)




     
     
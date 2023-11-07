class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


#Recursively traverses two binary trees comparing them at each level
def similar(r1, r2):
    if r1 == None and r2 == None:
        return True

    if r1 != None and r2 != None:
        return (r1.val == r2.val and similar(r1.left, r2.left) and similar(r1.right, r2.right))

    return False

root1 = TreeNode()
root2 = TreeNode()
node1 = TreeNode()
node2 = TreeNode()
node3 = TreeNode()
node4 = TreeNode()
node5 = TreeNode()
node6 = TreeNode()

root1.val = 0
root2.val = 0

node1.val = 1
node2.val = 2
node3.val = 3
node4.val = 1
node5.val = 2
node6.val = 3 

root1.left = node1
root1.right = node2
node1.left = node3

root2.left = node4
root2.right = node5
#difference
node4.right = node6

print(similar(root1,root2))
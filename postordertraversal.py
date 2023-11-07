class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):
    if root == None:
        return 

    postorderTraversal(root.left)

    postorderTraversal(root.right)

    print(root.val)

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

postorderTraversal(root)
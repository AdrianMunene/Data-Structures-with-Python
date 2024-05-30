class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# def postorderTraversal(root):
#     if root == None:
#         return 

#     postorderTraversal(root.left)

#     postorderTraversal(root.right)

#     print(root.val)
def peek(stack): 
    if len(stack) > 0: 
        return stack[-1] 
    return None

    
def postOrderIterative(root): 
         
    # Check for empty tree 
    if root is None: 
        return
 
    stack = [] 
     
    while(True): 
         
        while (root): 
            # Push root's right child and then root to stack 
            if root.right is not None: 
                stack.append(root.right) 
            stack.append(root) 
 
            # Set root as root's left child 
            root = root.left 
         
        # Pop an item from stack and set it as root 
        root = stack.pop() 
 
        # If the popped item has a right child and the 
        # right child is not processed yet, then make sure 
        # right child is processed before root 
        if (root.right is not None and
            peek(stack) == root.right): 
            stack.pop() # Remove right child from stack 
            stack.append(root) # Push root back to stack 
            root = root.right # change root so that the 
                            # right childis processed next 
 
        # Else print root's data and set root as None 
        else: 
            ans.append(root.data) 
            root = None
 
        if (len(stack) <= 0): 
                break


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

# postorderTraversal(root)
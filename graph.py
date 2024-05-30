class TreeNode():
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, data=0, neighbours=None):
        self.data = data
        self.neighbours = neighbours

nodeA = TreeNode({'A':'Blue'}, {'B':'Green', 'C':'Red'})

# nodeB = TreeNode()
# nodeB.data = {'B':'Green'}

attributes = vars(nodeA)

for k, v in attributes.items():
    print(f"{k}:{v}")


class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if(self.val == None):
            self.val = val
            return 
        if(self.val == val): return "no duplicates allowed"
        if(val < self.val and self.left == None): 
            self.left = BSTNode(val)
            return 
        if(val < self.val and self.left != None): 
            self.left.insert(val)
        if(val > self.val and self.right == None):
            self.right = BSTNode(val)
            return 
        if(val > self.val and self.right != None):
            self.right.insert(val)
            return 




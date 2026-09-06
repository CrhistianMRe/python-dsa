from typing import Any


class BSTNode:
    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:

        if(self.val == None):
            self.val = val
            return

        if(self.val == val): return

        if(val < self.val and self.left == None): 
            self.left = BSTNode(val)
            return

        if(val < self.val and not (self.left == None)): 
            BSTNode.insert(self.left, val)
            return

        if(val > self.val and self.right == None): 
            self.right = BSTNode(val)
            return

        if(val > self.val and not (self.right == None)): 
            BSTNode.insert(self.right, val)
            return





from typing import Any


class BSTNode:
    def height(self) -> int:
        if(self.val == None): return 0

        heightLeft = 0
        heightRight = 0

        if(not(self.left == None)):
            heightLeft = self.left.height()

        if(not(self.right == None)):
            heightRight = self.right.height()

        return max(heightLeft, heightRight) + 1;


    # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)


from typing import Any


class BSTNode:
    def exists(self, val: Any) -> bool:
        doesExist = False

        if(self.val == val):
            doesExist = True

        if(not(self.left == None) and not doesExist):
            doesExist = self.left.exists(val)

        if(not(self.right == None) and not doesExist):
            doesExist = self.right.exists(val)

        return doesExist


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


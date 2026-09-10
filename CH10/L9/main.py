from typing import Any


class BSTNode:
    def postorder(self, visited: list[Any]) -> list[Any]:
        if(not (self.left == None)):
            self.left.postorder(visited)

        if(not (self.right == None)):
            self.right.postorder(visited)


        if(not (self.val == None)):
            visited.append(self.val)

        return visited


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


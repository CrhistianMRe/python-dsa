from main import *

def ref_implementation(self, val):
    if not self.val:
        self.val = val
        return

    if self.val == val:
        return

    if val < self.val:
        if self.left:
            ref_implementation(self.left, val)
            return
        self.left = BSTNode(val)
        return

    if self.right:
        ref_implementation(self.right, val)
        return
    self.right = BSTNode(val)


def ref_inorder(self, visited):
    if self.left:
        visited = ref_inorder(self.left, visited)
    visited.append(self.val)
    if self.right:
        visited = ref_inorder(self.right, visited)
    return visited

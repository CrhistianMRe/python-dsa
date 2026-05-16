class BSTNode:
    def delete(self, val):
        if(self.val == None): return None

        rightExists = self.right != None
        leftExists = self.left != None

        if(val < self.val):
            if(leftExists):
                self.left = self.left.delete(val)
            return self

        if(val > self.val):
            if(rightExists):
                self.right = self.right.delete(val)
            return self

        if(val == self.val):
            if(not rightExists):
                return self.left
            if(not leftExists):
                return self.right
            if(leftExists and rightExists):
                temp = self.right
                while(temp.left != None):
                    temp = temp.left

                self.val = temp.val
                self.right = self.right.delete(self.val)
                return self
                
                










    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
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

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val


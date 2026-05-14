class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        length = len(self.items)

        if(length == 0): return None
        return self.items[length -1]

    def pop(self):
        length = len(self.items)

        if(length == 0): return None
        item = self.items[length - 1]
        self.items.pop(length -1)
        return item


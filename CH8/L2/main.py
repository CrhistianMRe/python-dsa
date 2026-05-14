class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if(not self.items): return None
        item = self.items[self.size() - 1]
        self.items.pop()
        return item

    def peek(self):
        if(not self.items): return None
        return self.items[self.size() - 1]

    def size(self):
        return len(self.items)

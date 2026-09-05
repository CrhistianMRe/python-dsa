from node import Node


class LinkedList:
    def add_to_head(self, node: Node) -> None:
        if(self.head == None): self.tail = node
        node.set_next(self.head)
        self.head = node

    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            self.tail = node
            return

        self.tail.set_next(node)
        self.tail = self.tail.next 


    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None

    # don't touch below this line

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)


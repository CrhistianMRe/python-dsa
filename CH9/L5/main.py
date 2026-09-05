from node import Node


class LinkedList:

    def add_to_tail(self, node: Node) -> None:
        if(self.head == None): 
            self.head = node
            return

        tail = self.head 

        for i in self:
            tail = i  

        tail.next = node


    # don't touch below this line

    def __init__(self) -> None:
        self.head: Node | None = None

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


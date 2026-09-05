from node import Node


class LinkedList:
    head: Node | None

    def __init__(self) -> None:
        self.head = None

    def __iter__(self):
        temp = self.head
        while(not (temp == None)):
            yield temp
            temp = temp.next

    # don't touch below this line

    def __repr__(self) -> str:
        nodes = []
        current = self.head
        while current and hasattr(current, "val"):
            nodes.append(current.val)
            current = current.next
        return " -> ".join(nodes)


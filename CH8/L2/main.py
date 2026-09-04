from typing import Any


class Queue:
    def __init__(self) -> None:
        self.items: list[Any] = []

    def push(self, item: Any) -> None:
        self.items.insert(0, item)

    def pop(self) -> Any:
        if(self.size() == 0): return None
        return self.items.pop(self.size() - 1)

    def peek(self) -> Any:
        if(self.size() == 0): return None
        return self.items[self.size() -1]

    def size(self) -> int:
        return len(self.items)


from typing import Any


class Stack:
    def __init__(self, *args) -> None:
        self.top = None
        self.size = 0
        for arg in args:
            self.push(arg)

    def push(self, data: Any) -> None:
        self.top = Node(data, self.top)
        self.size += 1

    def pop(self) -> Any:
        if self.isEmpty():
            raise IndexError('pop from empty stack')
        x = self.top
        self.top = self.top.next
        self.size -= 1
        return x

    def getTop(self) -> Any:
        if self.isEmpty():
            raise IndexError('empty stack has not top element')
        return self.top.data

    def isEmpty(self) -> bool:
        return self.size == 0

    def clear(self) -> None:
        self.__init__()

    def __str__(self) -> str:
        result = ''
        node = self.top
        for _ in range(len(self)):
            result += str(node.data) + ', '
            node = node.next
        return result[:-2]

    def __len__(self) -> int:
        return self.size


class Node:
    def __init__(self, data: Any, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

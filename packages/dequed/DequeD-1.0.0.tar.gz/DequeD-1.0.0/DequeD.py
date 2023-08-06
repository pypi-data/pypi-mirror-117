from typing import Any


class Deque:
    def __init__(self, *args) -> None:
        self.head = None
        self.tail = None
        self.size = 0
        for arg in args:
            self.pushBack(arg)

    def pushFront(self, x: Any) -> None:
        NewNode = Node(x, prev=None, next=self.head)
        if self.isEmpty():
            self.tail = NewNode
        else:
            self.head.prev = NewNode
        self.head = NewNode
        self.size += 1

    def pushBack(self, x: Any) -> None:
        NewNode = Node(x, prev=self.tail, next=None)
        if self.isEmpty():
            self.head = NewNode
        else:
            self.tail.next = NewNode
        self.tail = NewNode
        self.size += 1

    def popFront(self) -> Any:
        if self.isEmpty():
            raise IndexError('pop from empty deque')
        data = self.head.data
        self.head = self.head.next
        if self.size == 1:
            self.tail = None
        self.size -= 1
        return data

    def popBack(self) -> Any:
        if self.isEmpty():
            raise IndexError('pop from empty deque')
        data = self.tail.data
        self.tail = self.tail.prev
        if self.size == 1:
            self.head = None
        self.size -= 1
        return data

    def isEmpty(self) -> bool:
        return self.size == 0

    def __str__(self) -> str:
        result = ''
        node = self.head
        for _ in range(len(self)):
            result += str(node) + ', '
            node = node.next
        return '<' + result[:-2] + '>'

    def __len__(self) -> int:
        return self.size


class Node:
    def __init__(self, data: Any, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        if type(self.data) == str:
            return "'" + self.data + "'"
        else:
            return str(self.data)

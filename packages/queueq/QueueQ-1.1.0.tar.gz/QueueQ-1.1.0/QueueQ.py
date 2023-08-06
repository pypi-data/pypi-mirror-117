class Queue:
    def __init__(self, *args) -> None:
        self.first = None
        self.last = None
        self.size = 0
        for arg in args:
            self.push(arg)

    def push(self, data) -> None:
        if self.first is None:
            self.first = Node(data)
            self.last = self.first
        else:
            self.last.next = Node(data)
            self.last = self.last.next
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError('pop from empty list')
        data = self.first
        self.first = self.first.next
        self.size -= 1
        return data

    def front(self):
        return self.first.data

    def back(self):
        return self.last.data

    def isEmpty(self) -> bool:
        return len(self) == 0

    def __str__(self) -> str:
        result = ''
        node = self.first
        for _ in range(self.size):
            result += str(node) + ', '
            node = node.next
        return result[:-2]

    def __len__(self) -> int:
        return self.size


class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

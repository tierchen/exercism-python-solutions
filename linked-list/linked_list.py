class Node:
    def __init__(self, value, next_=None, previous=None):
        self.value = value
        self.next = next_
        self.previous = previous


class LinkedList:
    def __init__(self):
        self._length = 0
        self._head = None
        self._tail = None

    def __len__(self):
        return self._length

    def __iter__(self):
        current = self._tail
        for _ in range(len(self)):
            yield current.value
            current = current.previous

    def pop(self):
        if len(self) == 0:
            raise EmptyList
        value, node = self._head.value, self._head
        self._head = self._head.next
        del node
        self._length -= 1
        return value

    def push(self, value):
        node = Node(value, next_=self._head)
        if len(self) == 0:
            self._tail = node
        else:
            self._head.previous = node
        self._head = node
        self._length += 1

    def shift(self):
        if len(self) == 0:
            raise EmptyList
        value, node = self._tail.value, self._tail
        self._tail = self._tail.previous
        self._length -= 1
        del node
        return value

    def unshift(self, value):
        node = Node(value, previous=self._tail)
        if len(self) == 0:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._length += 1


class EmptyList(Exception):
    pass

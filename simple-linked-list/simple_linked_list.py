class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        if values is None:
            values = []
        self._head = None
        self._length = 0

        for value in values:
            self.push(value)

    def __len__(self):
        return self._length

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.value()
            current = current.next()

    def head(self):
        if self._head is None:
            raise EmptyListException('Linked list is empty')
        return self._head

    def push(self, value):
        n = Node(value, self._head)
        self._head = n
        self._length += 1

    def pop(self):
        n = self._head
        if n is None:
            raise EmptyListException('Linked list is empty')
        self._head = self._head.next()
        self._length -= 1
        return n.value()

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    pass

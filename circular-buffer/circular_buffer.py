from collections import deque


class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self._storage = deque(maxlen=capacity)

    def write(self, value):
        if len(self._storage) == self._storage.maxlen:
            raise BufferFullException('Buffer is full')
        self._storage.append(value)

    def overwrite(self, value):
        self._storage.append(value)

    def read(self):
        if len(self._storage) == 0:
            raise BufferEmptyException('Buffer is empty')
        return self._storage.popleft()

    def clear(self):
        self._storage.clear()

import operator as op


class Record:
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Tree:
    def __init__(self, graph, pointer=0):
        self._graph = graph
        self._pointer = pointer

    @classmethod
    def from_records(cls, records):
        if not records:
            return None
        root = records.pop(0)

        if (not root.record_id == root.parent_id == 0
                or any(record.record_id <= record.parent_id for record in records)
                or set(record.record_id for record in records) != set(range(1, len(records)+1))):
            raise ValueError('Wrong record structure')

        graph = [[] for i in range(len(records) + 1)]
        for record in records:
            graph[record.parent_id].append(record.record_id)
        return cls(graph)

    @property
    def children(self):
        return [Tree(self._graph, pointer=child_id) for child_id in self._graph[self._pointer]]

    @property
    def node_id(self):
        return self._pointer


def BuildTree(records):
    records.sort(key=op.attrgetter('record_id'))
    return Tree.from_records(records)

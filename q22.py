# Nó para alocação de uma Fila
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Classe que define uma Fila
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0


    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last =node

        if self.first is None:
            self.first = node

        self._size = self._size + 1


    def pop(self):
        if self.first is not None:
            pass
        raise  IndexError('pop from empty queue')




    def __len__(self):
        return self._size


    def __repr__(self):


    def __str__(self):
        return self.__repr__()
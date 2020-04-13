class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'

    __str__ = __repr__

    def __eq__(self, other):
        return self.value == other.value

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node

    @property
    def tail(self):
        node_ = self.head
        while node_.next is not None:
            node_ = node_.next
        return node_

    def to_list(self):
        return [item for item in self]

    def __iter__(self):
        node_ = self.head
        while True:
            if node_ is None:
                break
            yield node_
            node_ = node_.next

    def __len__(self):
        len_ = 0
        for item in self:
            len_ += 1
        return len_

    def __repr__(self):
        pass

    @classmethod
    def from_list(cls, nodes):
        list_ = cls()
        for node in nodes:
            list_.append(node)
        return list_
    
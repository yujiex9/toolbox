class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_node):
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

    def is_empty(self):
        return self.head is None

    def reverse(self):
        if self.is_empty():
            return

        prior_node = self.head
        current_node = prior_node.next
        while current_node is not None:
            prior_node.next = current_node.next
            current_node.next = self.head
            self.head = current_node
            current_node = prior_node.next

    def _get_entry_node_from_loop(self, meeting_node):
        node_starts_head = self.head
        node_starts_meeting_node = meeting_node
        while node_starts_head != node_starts_meeting_node:
            node_starts_head = node_starts_head.next
            node_starts_meeting_node = node_starts_meeting_node.next
        return node_starts_head

    def has_loop(self):
        res = (False, None)
        if self.is_empty():
            return res
        node = faster_node = self.head
        while faster_node.next is not None and faster_node.next.next is not None:
            node = node.next
            faster_node = faster_node.next.next
            if node == faster_node:
                entry_node = self._get_entry_node_from_loop(node)
                res = (True, entry_node)
                break
        return res

    @property
    def tail(self):
        node_ = self.head
        while node_.next is not None:
            node_ = node_.next
        return node_

    def to_list(self):
        return [node for node in self]

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

    @classmethod
    def from_list(cls, nodes):
        list_ = cls()
        for node in nodes:
            list_.append(node)
        return list_
    
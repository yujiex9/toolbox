import reprlib

from data_structures.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, new_node):
        new_node = self._to_node(new_node)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

    def pop(self):
        if self.is_empty():
            return
        current_node = self.head
        next_node = current_node.next
        while next_node is not None and next_node.next is not None:
            current_node = next_node
            next_node = next_node.next
        if current_node is self.head:
            retval = current_node
            self.head = None
        else:
            retval = next_node
            current_node.next = None
        return retval

    def remove(self, node):
        if self.is_empty():
            return
        node = self._to_node(node)
        prior_node = self.head
        # remove head
        if node == prior_node:
            self.head = prior_node.next
        else:
            current_node = prior_node.next
            while current_node is not None:
                if node == current_node:
                    prior_node.next = current_node.next
                    current_node.next = None
                    break
                prior_node = current_node
                current_node = current_node.next

    def is_empty(self):
        return self.head is None

    def _to_node(self, obj):
        """
        Convert an input object to a Node
        """
        if isinstance(obj, Node):
            return obj
        else:
            return Node(obj)

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

    def __contains__(self, node):
        for node_ in self:
            if node == node_:
                return True
        return False

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
        res = ', '.join(repr(node) for node in self)
        res = f'{self.__class__.__name__}({res})'
        if len(res) >= 80:
            return reprlib.repr(res)
        else:
            return res

    @classmethod
    def from_list(cls, nodes):
        list_ = cls()
        for node in nodes:
            list_.append(node)
        return list_

import pytest
from copy import deepcopy
from data_structures.linkedlist import LinkedList
from data_structures.node import Node


@pytest.fixture
def linkedlist():
    nodes = [Node(2), Node(3), Node('a'), Node(('e', 5))]
    return LinkedList.from_list(nodes)


def test_linkedlist_to_list(linkedlist):
    assert linkedlist.to_list() == [Node(2), Node(3), Node('a'), Node(('e', 5))]


def test_linkedlist_contains(linkedlist):
    assert Node(('e', 5)) in linkedlist


def test_linkedlist_pop(linkedlist):
    list_ = deepcopy(linkedlist)
    assert Node(('e', 5)) == list_.pop()

    size = len(list_)
    for i in range(size):
        list_.pop()
    
    assert len(list_) == 0


def test_linkedlist_remove(linkedlist):
    list_ = deepcopy(linkedlist)

    list_.remove(Node('a'))
    assert len(list_) == 3

    list_.remove(Node(2))
    assert list_.head == Node(3)


def test_linkedlist_revert(linkedlist):
    list_ = deepcopy(linkedlist)
    list_.reverse()
    assert [Node(('e', 5)), Node('a'), Node(3), Node(2)] == [node for node in list_]

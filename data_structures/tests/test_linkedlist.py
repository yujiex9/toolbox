from copy import deepcopy
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


@pytest.mark.parametrize(
    ['nodes', 'expected'],
    [
        ([Node(2)], [Node(2)]),
        ([Node('a'), Node(3)], [Node(3), Node('a')]),
        ([Node(2), Node(3), Node('a'), Node(('e', 5))], [Node(('e', 5)), Node('a'), Node(3), Node(2)])
    ]
)
def test_linkedlist_reverse(nodes, expected):
    _linkedlist = LinkedList.from_list(nodes)
    _linkedlist.reverse()
    nodes.reverse()
    assert nodes == [node for node in _linkedlist]


def test_linkedlist_has_loop():
    node_1 = Node('a')
    node_2 = Node('b')
    node_3 = Node('c')
    node_4 = Node('d')
    node_5 = Node('e')
    node_6 = Node('f')
    node_7 = Node('g')
    linkedlist_ = LinkedList.from_list([node_1, node_2, node_3, node_4, node_5, node_6, node_7])
    node_7.next = node_3
    assert (True, node_3) == linkedlist_.has_loop()


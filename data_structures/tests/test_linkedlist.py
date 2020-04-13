import pytest
from data_structures.linkedlist import LinkedList
from data_structures.node import Node


@pytest.fixture
def nodes():
    return [Node(2), Node(3), Node('a'), Node(('e', 5))]

def test_basic_linkedlist(nodes):
    linked_list = LinkedList.from_list(nodes)
    
    assert linked_list.to_list() == nodes

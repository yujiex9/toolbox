import random

import pytest
from data_structures.stack import Stack


def test_basic_stack_funcs():
    stack = Stack()
    assert stack.is_empty()
    stack.push(2)
    stack.push('a')
    stack.push(('e', 3))
    assert len(stack) == 3
    assert stack.peak == ('e', 3)
    assert [2, 'a', ('e', 3)] == stack.to_list()


def test_stack_bottom_up():
    list_ = [2, 3, 5, 7, 11]
    stack = Stack.from_list(list_)
    stack.bottom_up()
    assert 2 == stack.peak
    stack.bottom_up()
    assert 3 == stack.peak


def test_stack_reverse():
    list_ = [2, 3, 5, 7, 11]
    stack = Stack.from_list(list_)
    stack.reverse()
    assert [11, 7, 5, 3, 2] == stack.to_list()


def test_stack_sort():
    list_ = [1, 5, 3, 4, 2]
    stack = Stack.from_list(list_)
    stack.sort()
    assert [5, 4, 3, 2, 1] == stack.to_list()


def test_stack_caches_min_value():
    """
    O(1) time complexity to find the min value for a given stack
    """
    class MinStack:
        def __init__(self):
            self.__items_stack = Stack()
            self.__min_stack = Stack()

        def push(self, new_item):
            self.__items_stack.push(new_item)
            if self.__min_stack.is_empty():
                self.__min_stack.push(new_item)
            else:
                if new_item <= self.__min_stack.peak:
                    self.__min_stack.push(new_item)

        def pop(self):
            peak = self.__items_stack.pop()
            if peak == self.__min_stack.peak:
                self.__min_stack.pop()

        @property
        def min(self):
            return self.__min_stack.peak

    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(4)
    min_stack.push(6)
    min_stack.push(3)

    assert 3 == min_stack.min

    min_stack.pop()
    assert 4 == min_stack.min

    min_stack.pop()
    assert 4 == min_stack.min

    min_stack.pop()
    assert 5 == min_stack.min


@pytest.mark.parametrize(
    ['arriving_seq', 'popping_seq'],
    [
        ([2, 3, 5, 7, 11], [5, 3, 11, 7, 2]),
        ([2, 3, 5, 7, 11], [2, 7, 5, 3, 11]),
        ([2, 3, 5, 7, 11], [2, 3, 11, 7, 5]),
    ]
)
def test_stack_possible_popping_seq(arriving_seq, popping_seq):
    stack = Stack()

    index = 0
    for item in arriving_seq:
        stack.push(item)
        while stack.peak == popping_seq[index]:
            stack.pop()
            index += 1
            if index == len(popping_seq):
                break

    assert len(stack) == 0
    assert index == len(popping_seq)


def test_queue_impl_using_two_stacks():
    class Queue():
        def __init__(self):
            self.__pushing_stack = Stack()
            self.__popping_stack = Stack()

        def enqueue(self, new_item):
            self.__pushing_stack.push(new_item)

        def dequeue(self):
            if self.__popping_stack.is_empty():
                for i in range(len(self.__pushing_stack)):
                    self.__popping_stack.push(self.__pushing_stack.pop())
            ret = self.__popping_stack.pop()

            return ret

    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(5)
    assert 2 == queue.dequeue()
    assert 3 == queue.dequeue()
    queue.enqueue(7)
    assert 5 == queue.dequeue()
    assert 7 == queue.dequeue()

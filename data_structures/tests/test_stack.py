from data_structures.stack import Stack


def test_basic_stack_funcs():
    stack = Stack()
    assert stack.is_empty()
    stack.push(2)
    stack.push('a')
    stack.push(('e', 3))
    assert len(stack) == 3
    assert stack.peak == ('e', 3)


def test_stack_reverse():
    stack = Stack()
    list_ = [2, 3, 5, 7, 11]
    for value in list_:
        stack.push(value)
    size = len(stack)
    stack.reverse()
    assert list_ == [stack.pop() for i in range(size)]

import string
import pytest
from core import truncate


@pytest.fixture
def seq():
    return string.ascii_lowercase

@pytest.mark.parametrize(
    ['length', 'method', 'output'],
    [(10, 'lhs', '... uvwxyz'),
     (10, 'middle', 'abc ... yz'),
     (11, 'middle', 'abc ... xyz')]
)
def test_truncate(seq, length, method, output):
    res = truncate(seq, length, method)
    assert res == output

def test_truncate_default(seq):
    res = truncate(seq, 10)
    assert res == 'abcdef ...'

def test_truncate_with_value_error(seq):
    with pytest.raises(ValueError) as value_error:
        truncate(seq, 10, 'xuba')
    assert 'method should be either lhs, middle or rhs' == str(value_error.value)

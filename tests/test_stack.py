import pytest
from data_structures import stack

def test_push_and_pop():
    s = stack.Stack()
    s.push(10)
    s.push(20)

    assert s.pop() == 20
    assert s.pop() == 10
    assert s.pop() is None      

def test_pop_empty_stack():
    s = stack.Stack()
    assert s.pop() is None

def test_peek_does_not_remove():
    s = stack.Stack()
    s.push("alpha")
    s.push("beta")
    assert s.peek() == "beta"
    assert s.peek() == "beta"
    assert s.pop() == "beta"

def test_peek_empty_stack():
    s = stack.Stack()
    assert s.peek() is None

def test_is_empty_behavior():
    s = stack.Stack()
    assert s.is_empty() is True
    s.push("x")
    assert s.is_empty() is False
    s.pop()
    assert s.is_empty() is True 

def test_push_different_types():
    s = stack.Stack()
    s.push("orange")
    s.push(3.14)
    s.push([1,2])
    assert s.pop() == [1, 2]
    assert s.pop() == 3.14
    assert s.pop() == "orange"


@pytest.fixture
def prefilled_stack():
    s = stack.Stack()
    s.push(1)
    s.push(2)
    return s 

def test_prefilled_stack_pop(prefilled_stack):
    assert prefilled_stack.pop() == 2
    assert prefilled_stack.pop() == 1
    
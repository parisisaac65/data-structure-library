import pytest
from data_structures.heap import MinHeap

def test_push_pop():
    heap = MinHeap()
    heap.push(5)
    heap.push(3)
    heap.push(10)

    assert heap.pop() == 3
    assert heap.pop() == 5
    assert heap.pop() == 10
    assert heap.pop() is None      # empty heap

def test_is_empty():
    heap = MinHeap()
    assert heap.is_empty() is True
    heap.push(1)
    assert heap.is_empty() is False
    heap.pop()
    assert heap.is_empty() is True

def test_peek():
    heap = MinHeap()
    assert heap.peek() is None
    heap.push(42)
    assert heap.peek() == 42        # does not remove 
    assert heap.pop() == 42         # still there


def test_len():
    heap = MinHeap()
    assert len(heap) == 0
    heap.push(1)
    heap.push(2)
    assert len(heap) == 2
    heap.pop()
    assert len(heap) == 1
import pytest
from data_structures import queue_ds 

def test_enqueue_dequeue():
    q = queue_ds.Queue()
    q.enqueue(1)
    q.enqueue(2)

    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() is None      

def test_dequeue_empty():
    q = queue_ds.Queue()
    assert q.dequeue() is None

def test_peek():
    q = queue_ds.Queue()
    assert q.peek() is None

    q.enqueue(99)
    assert q.peek() == 99 

def test_mixed_operations():
    q = queue_ds.Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.peek() == "a"
    assert q.dequeue() == "a"
    q.enqueue("c")
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"
    assert q.dequeue() is None 

import pytest
from data_structures import linked_list

def test_append_and_remove():
    fruits = linked_list.LinkedList()
    fruits.insert_at_end("lychee")
    fruits.insert_at_end("pomegranate")

    values = list(fruits)
    assert values == ["lychee", "pomegranate"]
    assert repr(fruits) == "LinkedList(lychee -> pomegranate)"

def test_insert_at_beginning():
    fruits = linked_list.LinkedList()
    fruits.insert_at_beginning("pomegranate")
    fruits.insert_at_beginning("lychee")

    values = list(fruits)
    assert values == ["lychee", "pomegranate"]
    assert repr(fruits) == "LinkedList(lychee -> pomegranate)"

def test_remove_existing_node():
    fruits = linked_list.LinkedList()
    fruits.insert_at_end("lychee")
    fruits.insert_at_end("pomegranate")
    fruits.insert_at_end("raspberry")

    was_removed = fruits.remove("pomegranate")
    assert was_removed is True
    assert list(fruits) == ["lychee", "raspberry"]

def test_remove_head_node():
    fruits = linked_list.LinkedList()
    fruits.insert_at_end("lychee")
    fruits.insert_at_end("pomegranate")

    was_removed = fruits.remove("lychee")
    assert was_removed is True
    assert list(fruits) == ["pomegranate"]

def test_remove_nonexistent_value():
    fruits = linked_list.LinkedList()
    fruits.insert_at_end("lychee")
    assert fruits.remove("kiwi") is False

def test_remove_from_empty_list():
    fruits = linked_list.LinkedList()
    assert fruits.remove("lychee") is False

def test_is_empty():
    fruits = linked_list.LinkedList()
    assert fruits.is_empty() is True
    fruits.insert_at_end("lychee")
    assert fruits.is_empty() is False 

def test_iteration_and_repr():
    values = ["x", "y", "z"]
    items = linked_list.LinkedList()
    for v in values:
        items.insert_at_end(v)

    # __iter__ test
    assert list(items) == values

    # __repr__ test
    assert repr(items) == "LinkedList(x -> y -> z)"

import pytest
from data_structures.binary_search_tree import BinarySearchTree

def test_insert_and_in_order_traversal():
    bst = BinarySearchTree[int]()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)

    result = list(bst.in_order())
    assert result == [30, 50, 70]
    assert repr(bst) == "BinarySearchTree([30, 50, 70])"

def test_search_existing_and_nonexisting():
    bst = BinarySearchTree[str]()
    bst.insert("pear")
    bst.insert("apple")
    bst.insert("orange") 

    assert bst.search("apple") is True
    assert bst.search("banana") is False
    assert "orange" in bst
    assert "banana" not in bst

def test_remove_leaf_node(): 
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)

    assert bst.remove(5) is True
    assert list(bst.in_order()) == [10, 15]
    assert bst.remove(5) is False

def test_remove_node_with_one_child():
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)
    bst.insert(2)       # 2 is left child of 5

    assert bst.remove(5) is True
    assert list(bst.in_order()) == [2, 10]

def test_remove_node_with_two_children(): 
    bst = BinarySearchTree[int]()
    bst.insert(40)
    bst.insert(20)
    bst.insert(60)
    bst.insert(10)
    bst.insert(30)
    bst.insert(50)
    bst.insert(70)

    assert bst.remove(40) is True
    assert list(bst.in_order()) == [10, 20, 30, 50, 60, 70]
    assert bst.remove(40) is False      # Already deleted 

def test_remove_root_edge_cases():
    bst = BinarySearchTree[int]()

    # Case: root is the only node
    bst.insert(100)
    assert bst.remove(100) is True
    assert list(bst.in_order()) == []

    # Case: removing new root promoted from child
    bst.insert(10)
    bst.insert(5)
    assert bst.remove(10) is True
    assert list(bst.in_order()) == [5]

def test_pre_order_traversal():
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert list(bst.pre_order()) == [10, 5, 15]

def test_post_order_traversal():
    bst = BinarySearchTree[int]()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    assert list(bst.post_order()) == [5, 15, 10]

def test_duplicate_insertion_is_ignored():
    bst = BinarySearchTree[int]()
    bst.insert(20)
    bst.insert(10)
    bst.insert(30)
    bst.insert(10)      # Duplicate

    assert list(bst.in_order()) == [10 , 20, 30]
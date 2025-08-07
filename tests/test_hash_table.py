import pytest
from data_structures.hash_table import HashMap

def test_put_and_get():
    hm = HashMap()
    hm.put("apple", 1)
    hm.put("banana", 2)

    assert hm.get("apple") == 1
    assert hm.get("banana") == 2
    assert hm.get("cherry") is None     # key not present

def test_update_existing_key(): 
    hm = HashMap()
    hm.put("key", "first")
    hm.put("key", "second")

    assert hm.get("key") == "second"

def test_remove_existing_key():
    hm = HashMap()
    hm.put("x", 42)
    assert hm.remove("x") is True
    assert hm.get("x") is None
    assert hm.remove("x") is False

def test_remove_nonexistent_key():
    hm = HashMap()
    assert hm.remove("ghost") is False

def test_representation_with_entries():
    hm = HashMap()
    hm.put("dog", "bark")
    hm.put("cat","meow")
    result = repr(hm)

    assert "dog: bark" in result
    assert "cat: meow" in result
    assert result.startswith("HashMap{")
    assert result.endswith("}")

def test_multiple_keys_same_bucket():
    """
    Force keys into the same bucket by mocking hash() to return the same index.
    """
    class FixedKey:
        def __init__(self, label):
            self.label = label
        def __eq__(self, other):
            return isinstance(other, FixedKey) and self.label == other.label
        def __hash__(self):
            return 0        # Force all keys to collide
        
    hm = HashMap()
    k1 = FixedKey("A")
    k2 = FixedKey("B")

    hm.put(k1, 10)
    hm.put(k2, 20)

    assert hm.get(k1) == 10
    assert hm.get(k2) == 20
    assert hm.remove(k1) is True
    assert hm.get(k1) is None
    assert hm.get(k2) == 20 
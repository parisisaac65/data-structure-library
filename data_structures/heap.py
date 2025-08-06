from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')

class MinHeap(Generic[T]):
    """
    MinHeap[T]: A type-annotated, generic min-heap implementation using a list-based binary heap.

    This heap is a complete binary tree supporting efficient insertion and extraction of the minimum element.
    The smallest element is always at the root.

    Usage: 
        >>> heap = MinHeap[int]()
        >>> heap.push(10)
        >>> heap.push(5)
        >>> heap.push(20)
        >>> heap.peek()
        5
        >>> heap.pop()
        5
        >>> heap.pop()
        10

    Decision Decisions: 
    - Generic and type-annotated for type safety and static analysis.
    - Backed by a 0-based Python list for compact storage.
    - Supports push (insert), pop (extract min), peek (get min), is_empty.
    - Works for any comparable type T.

    When to use: 
    - Efficient for repeated minimum extraction and insertion (e.g., priority queues, scheduling).
    - Use when you need O(log n) insertion and O(log n) removal of min, and O(1) access to min. 

    Time Complexity: 
    - push: O(log n)
    - pop: O(log n)
    - peek, is_empty: O(1)

    Space Complexity: 
    - O(n), where n is the number of elements.
    """

    def __init__(self) -> None: 
        self._data: List[T] = []

    def is_empty(self) -> bool: 
        """Returns True if the heap is empty, otherwise False."""
        return not self._data
    
    def push(self, value: T) -> None:
        """Inserts a value into the heap."""
        self._data.append(value)
        self._heapify_up(len(self._data) - 1)

    def pop(self) -> Optional[T]:
        """
        Removes and returns the smallest element from the heap.
        Returns None if the heap is empty. 
        """
        if self.is_empty():
            return None
        if len(self._data) == 1: 
            return self._data.pop()
        min_val = self._data[0]
        self._data[0] = self._data.pop()
        self._heapify_down(0)
        return min_val 
    
    def peek(self) -> Optional[T]: 
        """Returns the smallest element without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self._data[0]
    
    def _heapify_up(self, index: int) -> None:
        """
        Restores the heap property by moving the value at the given index
        upward through the tree, swapping with its parent until the min-heap 
        condition is satisfied. 

        Parameters: 
            index (int): Index of the newly inserted element. 
        """
        parent = (index - 1) // 2 
        if index > 0 and self._data[index] < self._data[parent]:
            self._data[index], self._data[parent] = self._data[parent], self._data[index]
            self._heapify_up(parent) 

    def _heapify_down(self, index: int) -> None:
        """
        Restores the heap property by moving the value at the given index
        downward through the tree, swapping with the smaller child until the
        min-heap condition is restored. 
        """
        n = len(self._data)
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < n and self._data[left] < self._data[smallest]:
            smallest = left
        if right < n and self._data[right] < self._data[smallest]:
            smallest = right
        if smallest != index:
            self._data[index], self._data[smallest] = self._data[smallest], self._data[index]
            self._heapify_down(smallest)

    def __len__(self) -> int: 
        """Number of elements in the heap."""
        return len(self._data)
    
    def __repr__(self) -> str:
        """Returns string representation of the heap as a list."""
        return f"MinHeap({self._data})"
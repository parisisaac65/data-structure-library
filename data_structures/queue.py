from typing import Generic, List, Optional, TypeVar

T = TypeVar('T')

class Queue(Generic[T]): 
    """
    Queue[T]: A type-annotated, generic queue implementation.

    Implementation Note: 
    This `Queue` class uses a Python list internally for simplicity and clarity, which makes `enqueue` operations O(1) but
    `dequeue` operation O(n) because removing from the front of a list requires shifting all other elements.
    For high-performance use cases, Python's built-in ``collections.deque`` is recommended because it supports fast appends
    and pops from both ends in O(1) time.

    This queue follows the FIFO (First In First Out) principle, where the first element to enter the queue is the first to be removed.
    It supports the essential FIFO operations: enqueue, dequeue, peek, and is_empty.
    This implementation uses Python's built-in list to store the elements.
    Use this queue when you need to manage data in a strict FIFO order, such as scheduling tasks, handling print jobs, or
    managing event queues. 

    Design decisions: 
    - **Type Safety:**: Uses Python's generics and type hints so the queue can store any consistent type, supporting static type
    checking and IDE tooling.
    - **Graceful Underflow:** Method returns `None` instead of raising errors when dequeuing or peeking from an empty queue,
    favoring ergonomic error handling over exceptions for simple integration. 
    - **Performance:** Enqueuing (adding) an item to the end of a Python list takes O(1) amortized time, but dequeuing (removing)
    from the front is O(n) due to list element shifting. 

    Usage:
        Basic usage: 
            >>> queue = Queue[int]()
            >>> queue.is_empty()
            True 
            >>> queue.enqueue(10)
            >>> queue.enqueue(20)
            >>> queue.peek()
            10
            >>> queue.dequeue()
            10
            >>> queue.is_empty()
            False
            >>> queue.dequeue()
            20 
            >>> queue.dequeue()     # empty now
            None

        High-performance alternative with ``collections.deque``:
            # At the top of your file: from collections import deque 
            >>> q = deque()
            >>> q.append(10)    # enqueue
            >>> q.popleft()     # dequeue     

    Time Complexity: 
    - Enqueue: O(1)
    - Dequeue: O(n) (due to list pop(0))
    - Peek: O(1)

    Space Complexity: 
    - O(n), where n is the number of items in the queue 
    """

    _items: List[T]     # Type annotation for the instance attribute 

    def __init__(self) -> None: 
        """Initialize an empty queue."""
        self._items = []

    def enqueue(self, item: T) -> None: 
        """
        Add an item to the back of the queue.

        Parameters: 
            item (T): The item to add.
        """
        self._items.append(item)

    def dequeue(self) -> Optional[T]: 
        """
        Remove and return the item at the front of the queue. 

        Returns: 
            Optional[T]: The front item, or None if the queue is empty. 
        """
        if self.is_empty():
            return None
        return self._items.pop(0)
    
    def peek(self) -> Optional[T]:
        """
        Return (but do not remove) the front item.

        Returns: 
            Optional[T]: The front item, or None if the queue is empty. 
        """
        if self.is_empty(): 
            return None
        return self._items[0]
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty. 

        Returns: 
            bool: True if empty, False otherwise. 
        """
        return len(self._items) == 0 


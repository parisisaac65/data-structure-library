from typing import Generic, List, Optional, TypeVar 

T = TypeVar('T')

class Stack(Generic[T]): 
    """
    Stack[T]: A type-annotated, generic stack implementation with detailed documentation. 

    This stack follows the LIFO (Last In First Out) principle, where the last element is the first to be removed.
    The standard LIFO operations (push, pop, peek, is_empty) are supported.
    This implementation uses Python's built-in list to stack elements. 
    Use this stack when you need to manage data with a strict LIFO order, such as parsing, undo/redo, and/or
    algorithm state. 

    Design decisions:
    - **Type Safety:** Uses Python's generics and type hints so the stack can store any consistent type, supporting
    static checkers and IDE tooling.
    - **Graceful Underflow:** Methods return `None` instead of raising for empty stack access, favoring
    ergonomic error-handling over exceptions for simple code integration. 
    - **Performance:** Adding (push) or removing (pop) an item at the end of a Python list takes O(1) amortized time. 

    Usage: 
        >>> stack = Stack[int]()
        >>> stack.is_empty()
        True
        >>> stack.push(42)
        >>> stack.push(99)
        >>> stack.peek()
        99
        >>> stack.pop()
        99
        >>> stack.pop()
        42
        >>> stack.pop()     # edge case: popping from empty stack 
        None
        >>> stack.is_empty()
        True 

    Edge Cases:
    - Calling `pop()` or `peek()` on an empty stack returns `None`.
    - Push and pop are both O(1) on typical Python interpreters. 

    When to use this over collections.deque:
    - When you primarily need LIFO behavior. 
    - When you mainly require to push and pop elements from the end. 
    - When you require fast and random access to elements by index. 


    Time Complexity: 
    - Push: O(1) amortized 
    - Pop: O(1) amortized 
    - Peek: O(1)

    Space Complexity: 
    - O(n), where n is the number of items 
    """
    
    _items: List[T]     # Type annotation for the instance attribute

    def __init__(self) -> None:
        """
        Initializes an empty stack.
        """
        self._items = [] 

    def push(self, item: T) -> None:
        """
        Pushes an item onto the top of the stack.

        Parameters:
            item (T): The item to add. 

        Returns:
            None

        Example:
            stack.push('Paris')
        """
        self._items.append(item)

    def pop(self) -> Optional[T]:
        """
        Removes and returns the top item. If the stack is empty, returns None. 

        Returns: 
            Optional[T]: The item that was on top, or None if empty. 

        Example: 
            >>> item = stack.pop()
            >>> if item is None: 
            ...     print("Stack was empty")
        """
        if not self._items:
            return None
        return self._items.pop()

    def peek(self) -> Optional[T]:
        """
        Returns (but does not remove) the top item, or None if the stack is empty.

        Returns:
            Optional[T]: The top item, or None if stack is empty.

        Example:
            top = stack.peek()
        """
        if not self._items:
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        """
        Checks if the stack is empty. 

        Returns: 
            bool: True if the stack is empty, False otherwise. 

        Example: 
            if stack.is_empty():
                print("No items left:")
        """
        return not self._items 

  
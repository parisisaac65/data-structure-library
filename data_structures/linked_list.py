from typing import Generic, Optional, TypeVar, Iterator

T = TypeVar('T')

class Node(Generic[T]):
    """
    Node[T]: Represents a node in a singly linked list.

    Attributes:
        data(T): The value stored in the node
        next (Optional[Node[T]]): Reference to the next node in the list or None if it is the last node. 
    """
    def __init__(self, data: T) -> None: 
        """
        Initializes a node with the given data and no next node. 

        Parameters:
            data (T): The data stored in the node. 
        """
        self.data: T = data 
        self.next: Optional['Node[T]'] = None

class LinkedList(Generic[T]): 
    """
    LinkedList[T]: A type-annotated, generic singly linked list implementation with detailed documentation. 

    This linked list provides operations to add, remove, and iterate over elements. 
    It maintains a head pointer to the first node in the list. 

    Usage: 
        >>> linked_list = LinkedList[int]()
        >>> linked_list.is_empty()
        True
        >>> linked_list.insert_at_end(10)
        >>> linked_list.insert_at_beginning(5)
        >>> list(linked_list)
        [5, 10]
        >>> linked_list.remove(5)
        True
        >>> list(linked_list)
        [10]

    Design Decisions: 
    - Generic and type-annoated for type safety and static analysis. 
    - Single linked list (each node points only to the next).
    - Methods return meaningful values for success/failure states.
    - Iteration support to allow convenient list traversal. 

    When to use: 
    - For frequent insertions/deletions at the list start or middle without resizing overhead.
    - When you don't need fast random access (prefer Python lists for that).
    - For memory-flexible node allocation, trading higher per-node memory cost.
    - For double-ended queues, consider `collections.deque` instead.

    Time Complexity: 
    - insert_at_beginning: O(1)
    - insert_at_end: O(n)
    - remove: O(n)
    - is_empty: O(1)
    - iteration (__iter__): O(n)

    Space Complexity: 
    - O(n), where n is the number of nodes
    """

    def __init__(self) -> None: 
        """
        Initializes an empty linked list.
        """
        self.head: Optional[Node[T]] = None

    def is_empty(self) -> bool: 
        """
        Checks if the linked list is empty.

        Returns: 
            bool: True if the list is empty, False otherwise. 

        Example: 
            if linked_list.is_empty():
                print("List is empty")
        """
        return self.head is None 
    
    def insert_at_beginning(self, data: T) -> None: 
        """
        Inserts a new node with the given data at the beginning of the list. 

        Parameters: 
            data (T): The data to insert. 

        Example: 
            linked_list.insert_at_beginning(42)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: T) -> None: 
        """
        Inserts a new node with the given data at the end of the list.

        Parameters: 
            data (T): The data to insert. 

        Example: 
            linked_list.insert_at_end(99)
        """
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
            return 
        
        current = self.head 
        while current.next: 
            current = current.next
        current.next = new_node 
    
    def remove(self, data: T) -> bool: 
        """
        Removes the first node containing the specified data. 

        Parameters: 
            data (T): The data to remove.

        Returns: 
            bool: True if a node was removed, False if no matching node was found.

        Example: 
            removed = linked_list.remove(42)
            if removed:
                print("Node removed")
            else: 
                print("Node not found")
        """
        current = self.head
        previous = None 

        while current: 
            if current.data == data:
                if previous is None: 
                    # Removing head node
                    self.head = current.next 
                else: 
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        
        return False 
    
    def __iter__(self) -> Iterator[T]:
        """
        Iterates over the elements of the linked list.

        Yields: 
            Iterator[T]: The data of each node in order. 

        Example: 
            for value in linked_list:
                print(value)
        """
        current = self.head
        while current: 
            yield current.data
            current = current.next

    def __repr__(self) -> str: 
        """
        Returns a string representation of the linked list.

        Returns:
            str: String showing nodes in order, separated by arrows. 

        Example: 
            print(linked_list)
            # Output: LinkedList(5 -> 10 -> 15)
        """
        values = list(self)
        return f"LinkedList({' -> '.join(map(str, values))})"
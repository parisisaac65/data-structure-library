from typing import Optional, Generic, TypeVar, Iterator

T = TypeVar('T')

class TreeNode(Generic[T]): 
    """
    TreeNode[T]: Represents a node in the binary search tree. 

    Attributes:
        data (T): The value contained in the node. 
        left (Optional[TreeNode[T]]): Left child node (values less than this node).
        right (Optional[TreeNode[T]]): Right child node (values greater than this node). 
    """
    def __init__(self, data: T) -> None:
        self.data: T = data
        self.left: Optional['TreeNode[T]'] = None
        self.right: Optional['TreeNode[T]'] = None

class BinarySearchTree(Generic[T]):
    """
    BinarySearchTree[T]: A type-annotated, generic binary search tree implementation. 

    This Binary Search Tree (BST) maintains the property that for any node, all values in the left
    subtree are less than the node's values and all values in the right subtree are greater. 

    Usage: 
        >>> bst = BinarySearchTree[int]()
        >>> bst.insert(50)
        >>> bst.insert(30)
        >>> bst.insert(70)
        >>> 50 in bst
        True
        >>> list(bst.in_order())
        [30, 50, 70]
        >>> bst.remove(30)
        True
        >>> list(bst.in_order())
        [50, 70]

    Design Decisions: 
    - Generic and type-annotated for type safety and static analysis. 
    - Supports insert, search, remove, and traversal operations. 
    - Iteration methods for in-order, pre-order, and post-order traversal. 
    - Raises no exceptions for removing/searching missing values; returns bool or None.

    Time Complexity (average): 
    - insert, search, remove: O(log n)
    - traversal: O(n)

    Space Complexity: 
    - O(n), where n is the number of nodes 
    """

    def __init__(self) -> None: 
        self.root: Optional[TreeNode[T]] = None

    def insert(self, value: T) -> None: 
        """
        Inserts a value into the BST.

        Parameters: 
            values (T): The value to insert. 
        """
        self.root = self._insert(self.root, value)

    def _insert(self, node: Optional[TreeNode[T]], value: T) -> TreeNode[T]:
        if node is None:
            return TreeNode(value)
        if value < node.data: 
            node.left = self._insert(node.left, value)
        elif value > node.data: 
            node.right = self._insert(node.right, value)
        # if value == node.data, do nothing (no duplicates)
        return node
    
    def search(self, value: T) -> bool: 
        """
        Searches for a value in the BST.

        Parameters: 
            value (T): The value to search for. 

        Returns: 
            bool: True if found, False otherwise.
        """
        return self._search(self.root, value)
    
    def _search(self, node: Optional[TreeNode[T]], value: T) -> bool: 
        if node is None:
            return False
        if value == node.data: 
            return True
        elif value < node.data: 
            return self._search(node.left, value)
        else: 
            return self._search(node.right, value)

    def remove(self, value: T) -> bool: 
        """
        Removes a value from the BST. 

        Parameters: 
            value (T): The value to remove. 

        Returns: 
            bool: True if the value existed and was removed, False otherwise. 
        """
        self.root, deleted = self._remove(self.root, value)
        return deleted 
    
    def _remove(self, node: Optional[TreeNode[T]], value: T) -> tuple[Optional[TreeNode[T]], bool]:
        if node is None: 
            return None, False
        
        deleted = False
        if value < node.data: 
            node.left, deleted = self._remove(node.left, value)
        elif value > node.data: 
            node.right, deleted = self._remove(node.right, value)
        else: 
            deleted = True
            # node with only one child or no child
            if node.left is None: 
                return node.right, deleted
            elif node.right is None: 
                return node.left, deleted
            # node with two children: 
            # get the inorder successor (smallest in the right subtree)
            successor = self._min_value_node(node.right)
            node.data = successor.data
            node.right, _ = self._remove(node.right, successor.data)

        return node, deleted
    
    def _min_value_node(self, node: TreeNode[T]) -> TreeNode[T]:
        current = node
        while current.left is not None: 
            current = current.left
        return current
    
    def in_order(self) -> Iterator[T]: 
        """
        Traverses the BST in in-order (left, root, right).

        Yields: 
            Iterator[T]: Values in sorted order.
        """
        yield from self._in_order(self.root)

    def _in_order(self, node: Optional[TreeNode[T]]) -> Iterator[T]: 
        if node is not None:
            yield from self._in_order(node.left)
            yield node.data
            yield from self._in_order(node.right)

    def pre_order(self) -> Iterator[T]: 
        """
        Traverses the BST in pre-order (root, left, right). 

        Yields: 
            Iterator[T]: Values in pre-order. 
        """
        yield from self._pre_order(self.root)

    def _pre_order(self, node: Optional[TreeNode[T]]) -> Iterator[T]:
        if node is not None: 
            yield node.data
            yield from self._pre_order(node.left)
            yield from self._pre_order(node.right)

    def post_order(self) -> Iterator[T]: 
        """
        Traverses the BST in post-order (left, right, root).

        Yields: 
            Iterator[T]: Values in post-order. 
        """
        yield from self._post_order(self.root)

    def _post_order(self, node: Optional[TreeNode[T]]) -> Iterator[T]:
        if node is not None: 
            yield from self._post_order(node.left)
            yield from self._post_order(node.right)
            yield node.data

    def __contains__(self, value: T) -> bool: 
        """
        Supports 'in' keyword for searching. 

        Returns True if value is in BST, else False. 
        """
        return self.search(value)
    
    def __repr__(self) -> str: 
        """
        Returns string representation of BST as sorted values list. 

        Example: 
            BinarySearchTree([10, 20, 30])
        """
        return f"BinarySearchTree({list(self.in_order())})"
    
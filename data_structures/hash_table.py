from typing import Generic, TypeVar, List, Optional, Tuple

K = TypeVar('K')
V = TypeVar('V')

class HashMap(Generic[K, V]): 
    """
    Hashmap[K, V]: A type-annotated, generic hash map implementation using separate chaining for collisions.

    This hash map is an associative data structure that maps unique keys to values, allowing efficient
    insertion, deletion, and lookup operations. 
    It uses a hash function to compute an index into buckets where key-value pairs are stored. 
    Collisions are handled via separate chaining (a list of entries in each bucket).
    Use this hash map when you need quick average-case access to data via unique keys, such as caching, 
    indexing, or implementing sets and dictionaries. 

    Usage: 
        >>> hashmap = HashMap[str, int]()
        >>> hashmap.put("one", 1)
        >>> hashmap.put("two", 2)
        >>> hashmap.get("one")
        1
        >>> hashmap.remove("two")
        True
        >>> hashmap.get("two") is None
        True 

    Design Decisions: 
    - Uses a fixed-size list of buckets (default size 100).
    - Buckets use Python lists to store key-value pairs (chaining).
    - Simple built-in hash() function combined with modulo for indexing. 
    - Methods return meaningful values for existence checks. 
    - Does not resize automatically (can be extended later).

    Time Complexity: 
    - put, get, remove: O(1) average, O(n) worst case (all keys collide in same bucket). 
    
    Space Complexity: 
    - O(n), where n is the number of entries. 
    
    """

    def __init__(self, size: int = 100) -> None: 
        """
        Initializes the hash map with a fixed number of buckets. 

        Parameters: 
            size(int): Number of buckets. Default is 100. 
        """
        self.size = size
        self.buckets: List[List[Tuple[K, V]]] = [[] for _ in range(size)]

    def _bucket_index(self, key: K) -> int: 
        """
        Computes the bucket index for a key. 

        Parameters: 
            key (K): The key to hash. 

        Returns: 
            int: The index of the bucket. 
        """
        return hash(key) % self.size
    
    def put(self, key: K, value: V) -> None:
        """
        Inserts or updates the value associated with the key.

        Parameters: 
            key (K): The key to insert/update.
            value (V): The value to associate with the key. 
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket): 
            if k == key: 
                bucket[i] = (key, value)    # Update existing
                return 
        bucket.append((key, value))     # Add new

    def get(self, key: K) -> Optional[V]:
        """
        Retrieves the value associated with the key. 

        Parameters: 
            key (K): The key to look up. 

        Returns: 
            Optional[V]: The value if found, else None. 
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for k, v in bucket: 
            if k == key: 
                return v
        return None
    
    def remove(self, key: K) -> bool: 
        """
        Removes the key-value pair with the specified key. 

        Parameters: 
            key (K): The key to remove. 

        Returns: 
            bool: True if removal was successful, False if key not found.
        """
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if k == key: 
                del bucket[i]
                return True
        return False
    
    def __repr__(self) -> str: 
        """
        Returns string representation of the hash map showing buckets and their key-value pairs. 

        Returns: 
            str: String describing the contents of the hash map. 
        """
        items = []
        for bucket in self.buckets: 
            items.extend(f"{k}: {v}" for k, v in bucket)
        return f"HashMap{{{', '.join(items)}}}"

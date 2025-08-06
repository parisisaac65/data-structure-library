from typing import Dict, Set, TypeVar, Generic, Optional 

T = TypeVar('T')

class Graph(Generic[T]):
    """
    Graph[T]: A type-annotated, generic graph implementation using an adjacency list. 

    This is an undirected graph, meaning edges connect nodes in both directions(if A is connected to B,
    then B is connected to A).
    Nodes can be of any type (e.g., integers, strings, tuples), as long as they can be used as dictionary keys.
    Edges are unweighted by default, but the structure is easily extensible to support weights. 

    Usage: 
        >>> g = Graph[int]()
        >>> g.add_node(1)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 3)
        >>> 2 in g 
        True
        >>> g.neighbors(2)
        {1, 3}
        >>> g.remove_edge(1, 2)
        >>> g.remove_node(3)

    Design Decisions: 
    - Uses an adjacency list for efficient storage and traversal. 
    - Generic and type-annotated for type safety and static analysis.
    - Undirected by default, but can be adapted for directed graphs.
    - Minimally opinionated, but can be extended to add weights, directions, etc. 

    Time Complexity: 
    - add_node, add_edge, remove_node, remove_edge: O(1) average
    - neighbors: O(1) average

    Space Complexity: 
    - O(V + E), where V is number of nodes and E is number of edges
    """

    def __init__(self) -> None:
        self._adjacency: Dict[T, Set[T]] = {}

    def add_node(self, node: T) -> None:
        """Adds a node to the graph."""
        if node not in self._adjacency:
            self._adjacency[node] = set()
    
    def add_edge(self, u: T, v: T) -> None: 
        """
        Adds an undirected edge between nodes u and v.
        If nodes do not exist, they are created. 
        """
        self.add_node(u)
        self.add_node(v)
        self._adjacency[u].add(v)
        self._adjacency[v].add(u)

    def remove_edge(self, u: T, v: T) -> None: 
        """Removes the undirected edge between u and v, if it exists."""
        if u in self._adjacency and v in self._adjacency[u]:
            self._adjacency[u].remove(v)
        if v in self._adjacency and u in self._adjacency[v]:
            self._adjacency[v].remove(u)

    def remove_node(self, node: T) -> None:
        """Removes a node and all its edges."""
        if node in self._adjacency: 
            for neighbor in list(self._adjacency[node]):
                self._adjacency[neighbor].remove(node)
            del self._adjacency[node]

    def neighbors(self, node: T) -> Set[T]:
        """Returns a set of neighbors of the given node."""
        return self._adjacency.get(node, set())
    
    def __contains__(self, node: T) -> bool: 
        """Returns True if node is in the graph."""
        return node in self._adjacency
    
    def nodes(self) -> Set[T]:
        """Returns a set of all nodes in the graph."""
        return set(self._adjacency.keys())
    
    def edges(self) -> Set[tuple[T, T]]:
        """Returns a set of undirected edges as (u, v) tuples (u <= v)."""
        edge_set = set()
        for u in self._adjacency: 
            for v in self._adjacency: 
                if u <= v: 
                    edge_set.add((u, v))
                else: 
                    edge_set.add((v, u))
        return edge_set
    
    def __repr__(self) -> str: 
        """Returns string representation of the graph as adjacency dictionary."""
        return f"Graph({self._adjacency})"

    
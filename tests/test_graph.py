import pytest
from data_structures.graph import Graph

def test_add_node_and_membership():
    g = Graph()
    g.add_node("A")
    g.add_node("B")

    assert "A" in g
    assert "B" in g
    assert "C" not in g

def test_add_edge_auto_adds_nodes():
    g = Graph()
    g.add_edge("X", "Y")

    assert "X" in g
    assert "Y" in g
    assert g.neighbors("X") == {"Y"}
    assert g.neighbors("Y") == {"X"}

def test_remove_edge():
    g = Graph()
    g.add_edge("A", "B")
    g.remove_edge("A", "B")

    assert g.neighbors("A") == set()
    assert g.neighbors("B") == set()

def test_remove_node_removes_edges_too():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.remove_node("A")

    assert "A" not in g
    assert g.neighbors("B") == set()
    assert g.neighbors("C") == set()

def test_neighbors_return_empty_if_missing():
    g = Graph()
    assert g.neighbors("unknown") == set()

def test_nodes_and_edges():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("B", "C")

    expected_nodes = {"A", "B", "C"}
    nodes = g.nodes()
    assert nodes == expected_nodes

    edges = g.edges()
    # Ensure each undirected edge is counted only one (order doesn't matter)
    assert ("A", "B") in edges or ("B", "A") in edges
    assert ("B", "C") in edges or ("C", "B") in edges
    assert len(edges) == 2

def test_repr():
    g = Graph()
    g.add_edge("D", "E")
    out = repr(g)
    assert out.startswith("Graph({")
    assert "'D'" in out and "'E'" in out

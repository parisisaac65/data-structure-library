# Data Structure Library 

# Overview:
A Python library implementing common data structures (Stack, Queue, Linked List, Hash Table, Binary Tree, Graph) with emphasis on clear, well-documented, and type-safe code. 

## Features
- Generic and type-annotated implementations using Python's typing module
- Comprehensive docstrings for each class and method
- Usage examples including edge cases
- Documentation generated with Sphinx compatible docstrings
- Thoughtful design and explanation of trade-offs

## Installation 
```
git clone https://github.com/your-username/data-structure-library.git
cd data-structure-library
pip install .
```

## Usage Example 
```
from stack import Stack

stack = Stack[int]()
stack.push(10)
stack.push(20)
print(stack.peek())  # Outputs: 20
print(stack.pop())   # Outputs: 20
print(stack.is_empty())  # Outputs: False

```

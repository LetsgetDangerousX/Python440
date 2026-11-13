from __future__ import annotations

from collections.abc import Iterator
from typing import Any


class ContainsLoopError(Exception):
    pass


class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next_node: Node | None = None

    def __iter__(self) -> Iterator[Any]:
        node = self
        visited = set()
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.add(node)
            yield node.data
            node = node.next_node

    @property
    def has_loop(self) -> bool:
        """
        A loop is when the exact same Node appears more than once in a linked list.
        >>> root_node = Node(1)
        >>> root_node.next_node = Node(2)
        >>> root_node.next_node.next_node = Node(3)
        >>> root_node.next_node.next_node.next_node = Node(4)
        >>> root_node.has_loop
        False
        >>> root_node.next_node.next_node.next_node = root_node.next_node
        >>> root_node.has_loop
        True
        >>> self_loop = Node(1)
        >>> self_loop.next_node = self_loop
        >>> self_loop.has_loop
        True
        >>> final_node_loop = Node(1)
        >>> final_node_loop.next_node = Node(2)
        >>> final_node_loop.next_node.next_node = final_node_loop.next_node
        >>> final_node_loop.has_loop
        True
        >>> duplicate_data = Node(5)
        >>> duplicate_data.next_node = Node(6)
        >>> duplicate_data.next_node.next_node = Node(5)
        >>> duplicate_data.next_node.next_node.next_node = Node(6)
        >>> duplicate_data.has_loop
        False
        """
        try:
            list(self)
            return False
        except ContainsLoopError:
            return True


if __name__ == "__main__":
    root_node = Node(1)
    root_node.next_node = Node(2)
    root_node.next_node.next_node = Node(3)
    root_node.next_node.next_node.next_node = Node(4)
    print(root_node.has_loop)  # False
    root_node.next_node.next_node.next_node = root_node.next_node
    print(root_node.has_loop)  # True

    root_node = Node(5)
    root_node.next_node = Node(6)
    root_node.next_node.next_node = Node(5)
    root_node.next_node.next_node.next_node = Node(6)
    print(root_node.has_loop)  # False

    root_node = Node(1)
    print(root_node.has_loop)  # False

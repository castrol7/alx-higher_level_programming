#!/usr/bin/python3
"""Defines the SinglyLinkedList class."""
from node import Node

class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initialize a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert a new node into the correct sorted position in the list.

        The list is sorted in increasing order.

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Convert the linked list to a string representation.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)

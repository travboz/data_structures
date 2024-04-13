class Node:
    """Node in a linked list."""

    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        """Set the next node in the linked list."""
        self.next = node

    def __repr__(self):
        return f"Node({self.val})"

    def __str__(self):
        return f"{self.val}"

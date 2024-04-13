from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    # O(1) just adjusting pointers
    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            return

        # non-empty list
        node.next = self.head
        self.head = node

    # O(n) because must traverse list
    def add_to_tail(self, node):
        # empty list
        if self.head is None:
            self.head = node
            return

        # non-empty list
        # find tail
        tail = self.head
        while tail.next is not None:
            tail = tail.next

        tail.set_next(node)

    ## helper functions
    # can now use in for loops
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []

        curr = self.head
        while curr and hasattr(curr, "val"):
            nodes.append(curr.val)
            curr = curr.next

        return " -> ".join(nodes)

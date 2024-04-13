from Node import Node


class LinkedList:
    """A linked list that tracks head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, node):
        # empty list
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # non-empty list
        node.set_next(self.head)
        self.head = node

    def remove_from_head(self):
        if self.head is None:
            return None

        old_head = self.head
        self.head = self.head.next

        # if the new self.head is None, then tail is too
        if self.head is None:
            self.tail = None

        return old_head

    def add_to_tail(self, node):
        # empty list
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # setting the current tail to point to new node
        self.tail.next = node
        # setting the tail to be our new node
        self.tail = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)

        return " -> ".join(nodes)

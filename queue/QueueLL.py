from Node import Node


class QueueLL:
    """A Queue implemented with a linked list that tracks head and tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, node):
        """O(1) time: `push_left`"""
        # empty list
        if self.head is None:
            self.head = node
            self.tail = node
            return

        # non-empty list
        node.set_next(self.head)
        self.head = node

    def remove_from_head(self):
        """O(1) time: `pop_left`"""
        if self.head is None:
            return None

        old_head = self.head
        self.head = self.head.next

        # if the new self.head is None, then tail is too
        if self.head is None:
            self.tail = None

        return old_head

    # O(n): `pop_right`
    def remove_from_tail(self):
        """O(n) time: `pop_right`"""
        if self.head is None:
            return None

        # if there's only one node in the list
        if self.head == self.tail:
            removed_node = self.head
            self.head = None
            self.tail = None
            return removed_node

        # list of size > 1
        # find the node before the tail
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next

        # curr points to the node before tail
        removed_node = curr.next  # hold tail for return
        curr.next = None  # new tail next is None
        self.tail = curr  # new tail = curr
        return removed_node  # return old tail

    def add_to_tail(self, node):
        """O(1) time: `push_right`"""
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
        """Usable in for-loop"""
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        """String representation of Queue"""
        nodes = []
        for node in self:
            nodes.append(str(node))

        return " -> ".join(nodes)


if __name__ == "__main__":
    q = QueueLL()

    for i in range(5):
        q.add_to_tail(Node(i + 1))
        print(f"Current queue: {q}")

    # print(f"Queue: {q}")

    print(f"Head of Queue is: {q.head.val}")
    print(f"Tail of Queue is: {q.tail.val}")

    q.remove_from_head()

    print(f"Current after removing an item: {q}")

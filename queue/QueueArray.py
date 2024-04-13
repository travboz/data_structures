class Queue:
    def __init__(self):
        self.items = []

    # O(n) because we need to shift all n-1 items up
    def push(self, item):
        self.items.insert(0, item)

    # O(1) because we use array indexing and remove the last element without impacting others
    def pop(self):
        if self.size() == 0:
            return None

        popped = self.items[-1]
        del self.items[-1]
        return popped

    # O(1) because array indexing
    def peek(self):
        if len(self.items) == 0:
            return None

        return self.items[-1]


## Important consideration:
# Search is O(n) because our item could be at the front
# of our queue, leading us to pop() all n items.

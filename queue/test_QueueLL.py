import unittest
from Node import Node
from QueueLL import QueueLL


class TestQueueLL(unittest.TestCase):

    def test_add_to_tail(self):
        q = QueueLL()
        for i in range(5):
            q.add_to_tail(Node(i + 1))
        self.assertEqual(str(q), "1 -> 2 -> 3 -> 4 -> 5")

    def test_remove_from_head(self):
        q = QueueLL()
        for i in range(5):
            q.add_to_tail(Node(i + 1))
        removed_node = q.remove_from_head()
        self.assertEqual(str(removed_node), "1")
        self.assertEqual(str(q), "2 -> 3 -> 4 -> 5")

    def test_remove_from_tail(self):
        q = QueueLL()
        for i in range(5):
            q.add_to_tail(Node(i + 1))
        removed_node = q.remove_from_tail()
        self.assertEqual(str(removed_node), "5")
        self.assertEqual(str(q), "1 -> 2 -> 3 -> 4")

    def test_add_to_head(self):
        q = QueueLL()
        for i in range(5):
            q.add_to_head(Node(i + 1))
        self.assertEqual(str(q), "5 -> 4 -> 3 -> 2 -> 1")

    def test_remove_from_empty_queue(self):
        q = QueueLL()
        removed_node = q.remove_from_head()
        self.assertIsNone(removed_node)

    def test_add_and_remove_alternatively(self):
        q = QueueLL()
        for i in range(5):
            q.add_to_tail(Node(i + 1))
            removed_node = q.remove_from_head()
            self.assertEqual(str(removed_node), str(i + 1))

    def test_empty_queue_after_removing_all_nodes(self):
        q = QueueLL()
        for i in range(5):
            q.add_to_tail(Node(i + 1))
        for i in range(5):
            q.remove_from_head()
        self.assertEqual(str(q), "")

    def test_add_to_empty_queue(self):
        q = QueueLL()
        q.add_to_tail(Node(1))
        self.assertEqual(str(q), "1")

    def test_remove_from_queue_with_single_node(self):
        q = QueueLL()
        q.add_to_tail(Node(1))
        removed_node = q.remove_from_head()
        self.assertEqual(str(removed_node), "1")
        self.assertEqual(str(q), "")

    def test_remove_from_tail_empty_queue(self):
        q = QueueLL()
        removed_node = q.remove_from_tail()
        self.assertIsNone(removed_node)

    def test_remove_from_tail_single_node(self):
        q = QueueLL()
        q.add_to_tail(Node(1))
        removed_node = q.remove_from_tail()
        self.assertEqual(str(removed_node), "1")
        self.assertEqual(str(q), "")


if __name__ == "__main__":
    unittest.main()

# Queue

This is an implementation of a Queue using both an Array and a Linked List.

The Linked List implementation allows for double ended operations and leads to faster push and pop operations because when elements are added or removed from the first index of the array all the items need to be shifted, which takes `O(n)` time. 

The time complexities below are reflective of the Linked List implementation of a Queue.

|Operation | Time Complexity | Method |
| --- | --- | ---| 
|`push_left` | `O(1)` | `add_to_head`|
|`push_right` | `O(1)` | `add_to_tail`|
|`pop_left` | `O(1)` | `remove_from_head` |
|`pop_right` | `O(n)` | `remove_from_tail` |

# Directory Structure: 
`Node.py`: Node for the linked list.

`QueueArray.py`: Array implementation of Queue.

`QueueLL.py`: Linked list implementation of Queue.

`test_QueueLL.py`: Unit tests for the linked list implementation of the Queue.


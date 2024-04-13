# Queue

This is an implementation of a Queue using both an Array and a Linked List.

The Linked List implementation allows for double ended operations and leads to faster push and pop operations because when elements are added or removed from the first index of the array all the items need to be shifted, which takes `O(n)` time. 

|Operation | Time Complexity | Method |
| --- | --- | ---| 
|`push_left` | `O(1)` | `add_to_head`|
|`push_right` | `O(1)` | `add_to_tail`|
|`pop_left` | `O(1)` | `remove_from_head` |
|`pop_right` | `O(n)` | `remove_from_tail` |
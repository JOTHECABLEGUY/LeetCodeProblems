"""23. Merge k Sorted Lists
Hard
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104."""

import pytest
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def test(self):
        return linkedlist_to_list(self.mergeKLists([list_to_linkedlist([1, 2, 3]), list_to_linkedlist([4, 5, 6])]))
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
            Merges k sorted linked lists into a single sorted linked list.

            This function takes a list of k sorted linked lists and merges them into one 
            sorted linked list. It collects all the values from the input lists, sorts them, 
            and then constructs a new linked list from the sorted values.

            Args:
                lists (List[Optional[ListNode]]): A list of linked lists to be merged.

            Returns:
                Optional[ListNode]: The head of the merged sorted linked list. 
                Returns None if all input lists are empty.
        """
        # list to hold elements of each linked list
        overall_list = []
        
        # add all elements from non-empty lists to the overall list
        for l in lists:
            if l is None:
                continue
            overall_list.extend(linkedlist_to_list(l))
        
        # sort the list and return the result built into a linked list
        overall_list.sort()
        return list_to_linkedlist(overall_list) if overall_list else None
    
def linkedlist_to_list(node:Optional[ListNode]) -> List[int]:
    """
        Converts a linked list to a Python list.

        This function takes the head of a linked list and iterates through the nodes,
        appending each node's value to a Python list. It returns the list containing 
        all the values from the linked list in the same order.

        Args:
            node (Optional[ListNode]): The head of the linked list to convert.

        Returns:
            List: A list containing the values of the linked list nodes.
    """
    
    # stores the list to be returned
    result = []
    
    # for all nodes, add the node's value to the result list and move to the next node
    while node:
        result.append(node.val)
        node = node.next
    
    # return the assembled list
    return result

def list_to_linkedlist(lst: Optional[List[int]]) -> Optional[ListNode]:
    """
        Converts a Python list to a linked list.

        This function takes a list of values and creates a linked list where each 
        element of the list corresponds to a node in the linked list. It returns 
        the head of the newly created linked list.

        Args:
            lst (List): A list of values to convert into a linked list.

        Returns:
            Optional[ListNode]: The head of the linked list created from the input list. 
            Returns None if the input list is empty.
    """
    
    # return None if the list is empty
    if not lst:
        return None
    
    # first node in linked list
    head = ListNode(lst[0])
    
    # assign the value of head to current
    current = head
    
    # build nodes from the list and append them to the end of the linked list
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    
    # return the first node in the linked list
    return head

@pytest.mark.parametrize(
    "lists, expected",
    [
        # Happy path tests
        pytest.param(
            [list_to_linkedlist([1, 4, 5]), list_to_linkedlist([1, 3, 4]), list_to_linkedlist([2, 6])],
            [1, 1, 2, 3, 4, 4, 5, 6]
        ),
        pytest.param(
            [list_to_linkedlist([1, 2, 3]), list_to_linkedlist([4, 5, 6]), list_to_linkedlist([7, 8, 9])],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ),
        # Edge cases
        pytest.param(
            [None, None, None],
            []
        ),
        pytest.param(
            [],
            []
        ),
        pytest.param(
            [list_to_linkedlist([])],
            []
        ),
        pytest.param(
            [list_to_linkedlist([1])],
            [1]
        ),
        pytest.param(
            [list_to_linkedlist([1, 3, 5]), list_to_linkedlist([]), list_to_linkedlist([2, 4, 6])],
            [1, 2, 3, 4, 5, 6]
        ),
        # Error cases
        pytest.param(
            [list_to_linkedlist([1, 2, 3]), None, list_to_linkedlist([4, 5, 6])],
            [1, 2, 3, 4, 5, 6]
        ),
    ],
    ids = [
        "three_sorted_lists",
        "three_non_overlapping_lists",
        "all_none_lists",
        "empty_list_of_lists",
        "single_empty_list",
        "single_element_list",
        "mixed_empty_and_non_empty_lists",
        "some_none_lists"
    ]
)
def test_mergeKLists(lists, expected):
    # Act
    result = Solution().mergeKLists(lists)

    # Assert
    assert linkedlist_to_list(result) == expected

if __name__ == "__main__":
    print(Solution().test())
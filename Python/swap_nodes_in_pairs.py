"""24. Swap Nodes in Pairs
Medium
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:



Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]


Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100"""

import pytest
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def test(self):
        return linkedlist_to_list(self.swapPairs(list_to_linkedlist([1, 2, 3, 4])))
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        overall_list = linkedlist_to_list(head)
        for i in range(0, len(overall_list)-1, 2):
            overall_list[i], overall_list[i+1] = overall_list[i+1], overall_list[i]
        head = list_to_linkedlist(overall_list)
        return head
    
def linkedlist_to_list(lst:Optional[ListNode]) -> List[int]:
    res = []
    while lst:
        res.append(lst.val)
        lst = lst.next
    return res

def list_to_linkedlist(lst:List[int]) -> Optional[ListNode]:
    if not lst:
        return None
    head = ListNode(lst[0])
    dummy = head
    for val in lst[1:]:
        dummy.next = ListNode(val)
        dummy = dummy.next
    return head

@pytest.mark.parametrize(
    "input_list, expected_list",
    [
        # Happy path tests
        ([1, 2, 3, 4], [2, 1, 4, 3]),  # even number of nodes
        ([1, 2, 3], [2, 1, 3]),        # odd number of nodes
        ([1], [1]),                    # single node
        ([], []),                      # empty list

        # Edge cases
        ([1, 2], [2, 1]),              # two nodes
        ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),  # odd number of nodes with more than 2 pairs

        # Error cases
        (None, None),                  # None input
    ],
    ids=[
        "even_number_of_nodes",
        "odd_number_of_nodes",
        "single_node",
        "empty_list",
        "two_nodes",
        "odd_number_of_nodes_with_more_than_2_pairs",
        "none_input",
    ]
)
def test_swapPairs(input_list, expected_list):
    # Arrange
    head = list_to_linkedlist(input_list)

    # Act
    result = Solution().swapPairs(head)

    # Assert
    assert linkedlist_to_list(result) == expected_list

if __name__ == "__main__":
    print(Solution().test())
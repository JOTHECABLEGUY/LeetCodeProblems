"""19. Remove Nth Node From End of List
Medium
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?"""
import pytest
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def test(self):
        nums = [1]
        return self.removeNthFromEnd(list_to_linkedlist(nums), 1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            Removes the nth node from the end of a linked list.

            This function takes the head of a linked list and an integer n, and removes the 
            nth node from the end of the list. It returns the head of the modified list.

            Args:
                head (Optional[ListNode]): The head of the linked list.
                n (int): The position of the node to remove from the end of the list.

            Returns:
                Optional[ListNode]: The head of the modified linked list after removing the nth node.
        """
        first_run = second_run = head
        for _ in range(n):
            if first_run is None:
                return head
            first_run = first_run.next
        if first_run is None:
            return head.next
        while first_run.next is not None:
            first_run = first_run.next
            second_run = second_run.next
        second_run.next = second_run.next.next
        return head
    
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
def list_to_linkedlist(lst):
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
@pytest.mark.parametrize(
    "head, n, expected",
    [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),  # happy path
        ([1], 1, []),  # single element list
        ([1, 2], 1, [1]),  # two elements, remove last
        ([1, 2], 2, [2]),  # two elements, remove first
        ([1, 2, 3], 3, [2, 3]),  # remove head
        ([1, 2, 3], 1, [1, 2]),  # remove tail
    ],
    ids=[
        "remove 2nd from end in [1,2,3,4,5]",
        "remove 1st from end in [1]",
        "remove 1st from end in [1,2]",
        "remove 2nd from end in [1,2]",
        "remove 3rd from end in [1,2,3]",
        "remove 1st from end in [1,2,3]",
    ]
)
def test_removeNthFromEnd(head, n, expected):
    # Act
    head_node = list_to_linkedlist(head)
    result_node = Solution().removeNthFromEnd(head_node, n)
    result_list = linkedlist_to_list(result_node)

    # Assert
    assert result_list == expected

@pytest.mark.parametrize(
    "head, n, expected",
    [
        ([], 1, []),  # empty list
        ([1], 2, [1]),  # n greater than list length
    ],
    ids=[
        "empty list",
        "n greater than list length",
    ]
)
def test_removeNthFromEnd_edge_cases(head, n, expected):
    # Act
    head_node = list_to_linkedlist(head) if head else None
    result_node = Solution().removeNthFromEnd(head_node, n)
    result_list = linkedlist_to_list(result_node)

    # Assert
    assert result_list == expected
    
if __name__ == "__main__":
    res = Solution().test()
    print(linkedlist_to_list(res))
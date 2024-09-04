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
from operator import index
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
        dummy = ListNode(val = nums[-1], next = None)
        for n in nums[-2::-1]:
            dummy = ListNode(val = n, next = dummy)
        return self.removeNthFromEnd(dummy, 1)
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
        if n == 0 or head is None:
            return head
        nodes = []
        while head is not None:
            nodes.append(head)
            head = head.next
        index_to_remove = len(nodes)-n
        if index_to_remove > len(nodes) or index_to_remove < 0:
            return nodes[0]

        # unlink from node to remove
        nodes[index_to_remove].next = None

        if index_to_remove == 0 and len(nodes) > 1:
            return nodes[1]
        if index_to_remove <= 0:
            return None
        nodes[index_to_remove-1].next = nodes[index_to_remove+1]if index_to_remove < len(nodes)-1 else None
        return nodes[0]
if __name__ == "__main__":
    res = Solution().test()
    while res is not None:
        if res.next is not None:
            print(res.val, '->', res.next.val)
        else:
            print(res.val)
        res = res.next
        
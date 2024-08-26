"""2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def extract_number_from_linked_list(self, ll):
        line = []
        while ll != None:
            line.append(str(ll.val))
            ll = ll.next
        return int("".join(line)[::-1])
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extracted_numbers = [self.extract_number_from_linked_list(l1), self.extract_number_from_linked_list(l2)]
        return self.build_list([int(c) for c in str(sum(extracted_numbers))])
    def build_list(self, nums: list[int]):
        node = ListNode(val = nums[0], next = None)
        for elem in nums[1:]:
            node = ListNode(val = elem, next = node)
        return node
    def test(self):
        test_1_lists = self.build_list([9, 4, 2]), self.build_list([9, 4, 6, 5])
        print(int(str(942+9465)))
        print(self.extract_number_from_linked_list(self.addTwoNumbers(test_1_lists[0], test_1_lists[1])))
if __name__ == "__main__":
    Solution().test()    
            
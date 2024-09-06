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
        return linkedlist_to_list(self.swapPairs(list_to_linkedlist([2, 1, 3])))
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            Swaps every two adjacent nodes in a linked list.

            This function modifies the linked list in place, rearranging the nodes such that each pair of adjacent nodes is swapped. 
            If the list has an odd number of nodes, the last node remains in its original position.

            Args:
                head (Optional[ListNode]): The head of the linked list to be modified.

            Returns:
                Optional[ListNode]: The head of the modified linked list after swapping pairs of nodes.
        """
        
        # return if the head or following node are empty
        if not head or not head.next:
            return head
        
        # dummy node to point to start of modified list
        dummy = ListNode(0)
        dummy.next = head
        
        # tail will be 1 node before current
        tail = dummy
        current = head
        
        #### EASIER TO EXPLAIN WITH EXAMPLE 2->1->3####
        # before the loop, the example list looks like: dummy -> 2 -> 1 -> 3
        #   with pointers dummy to dummy, tail to dummy, and current to node 2
        # during first iteration:
        #   temp will point to current.next.next, which is 2.next.next which is node 3
        #   tail.next = current.next, which makes dummy.next = 2.next, which means dummy -> 1 -> 2 -> 3
        #   current.next.next = current, meaning 2.next.next = 2, meaning 1.next = 2, linking 1 to 2
        #       making the list dummy -> 1 -> 2 -> 3
        #   current.next = temp, meaning 2.next = 3, linking 2 to 3: dummy -> 1 -> 2 -> 3
        #   tail = current, meaning tail gets reassigned to 2, advancing 2 spaces in the list since 2 was swapped forward
        #   current = temp, meaning current gets reassigned to 3, advancing 1 space in the list for the next swap
        
        # while there are at least 2 nodes remaining 
        while current and current.next:
            
            # get the node 2 ahead of current
            temp = current.next.next
            
            
            # set node after tail to be the node after current
            tail.next = current.next
            
            # remap the link of the node so that current will come before temp
            current.next.next = current
            current.next = temp
            
            # step tail and current up for next iteration
            tail = current
            current = temp
        
        # return the modified list by getting the nodes after dummy
        return dummy.next
    
def linkedlist_to_list(lst:Optional[ListNode]) -> Optional[List[int]]:
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
        (None, []),                  # None input
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
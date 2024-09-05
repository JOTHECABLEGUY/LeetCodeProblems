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

from heapq import heappush
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
    
    def merge_2_lists(self, l1, l2):
        """
            Merges two sorted linked lists into a single sorted linked list.

            This function takes two sorted linked lists and merges them into one sorted linked list. 
            It iterates through both lists, comparing their values and appending the smaller value to 
            the merged list, while also handling cases where one of the lists may be empty.

            Args:
                l1 (Optional[ListNode]): The head of the first sorted linked list.
                l2 (Optional[ListNode]): The head of the second sorted linked list.

            Returns:
                Optional[ListNode]: The head of the merged sorted linked list. 
                Returns None if any of the nodes contain non-integer values.
        """
        
        # if one list is empty, return the other. If both lists are empty, the first check will return None (the second list)
        if not l1:
            return l2
        if not l2:
            return l1
        
        # initialize a dummy and a head to point to the start of a new list
        dummy = head = ListNode()
        
        # while both lists are not empty
        while l1 and l2:
            
            # get the values and check that they are valid for comparison
            val1, val2 = l1.val, l2.val
            if not (isinstance(val1, int) and isinstance(val2, int)):
                return None
            
            # set the new list's next node to the lower value node and progress the list that node's list
            if val1 < val2:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            
            # move to next value for the new list to accept new nodes
            dummy = dummy.next
        
        # after one or both of the lists are consumed, add the remaining nodes from either list to the new list
        if l1:
            dummy.next = l1
        if l2:
            dummy.next = l2
        
        # return the first node in the new list
        return head.next
    
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
    
    def mergeKLists_2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
            Merges k sorted linked lists into a single sorted linked list.

            This function takes a list of k sorted linked lists and merges them into one 
            sorted linked list. It filters out any None values from the input list and 
            iteratively merges pairs of lists until only one merged list remains.

            Args:
                lists (List[Optional[ListNode]]): A list of linked lists to be merged.

            Returns:
                Optional[ListNode]: The head of the merged sorted linked list. 
                Returns None if all input lists are empty.
        """
        # filter out null lists as they should not be considered when sorting, return None if there are no valid lists
        if not (lists_to_merge := list(filter(lambda x: x is not None, lists))):
            return None
        
        # while there is more than 1 list available to merge, merge 2 at a time
        # and add the result to the end of the list, then remove the 2 lists that were just sorted.
        # This removes any extra sorting that is done by the iterative approach
        while len(lists_to_merge) > 1:
            merged = self.merge_2_lists(lists_to_merge[0], lists_to_merge[1])
            lists_to_merge.append(merged)
            lists_to_merge = lists_to_merge[2:]
        
        # return the head of the final sorted list
        return lists_to_merge[0]
            
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
    result = Solution().mergeKLists_2(lists)

    # Assert
    assert linkedlist_to_list(result) == expected

if __name__ == "__main__":
    print(Solution().test())
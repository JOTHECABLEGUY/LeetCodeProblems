"""21. Merge Two Sorted Lists
Easy
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""

from typing import Optional, List
import pytest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def test(self):
        l1, l2 = None,None
        return self.mergeTwoLists(list_to_linkedlist(l1), list_to_linkedlist(l2))
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            Merges two sorted linked lists into a single sorted linked list.

            This function takes two linked lists that are already sorted and merges them 
            into a new sorted linked list. It handles cases where one or both lists may 
            be empty and ensures that the values in the lists are integers.

            Args:
                list1 (Optional[ListNode]): The head of the first sorted linked list.
                list2 (Optional[ListNode]): The head of the second sorted linked list.

            Returns:
                Optional[ListNode]: The head of the merged sorted linked list. 
                Returns None if any of the nodes contain non-integer values.
        """
        
        # if the inputs are empty or None, return the other. (If both are not valid the first empty/None node will be returned)
        if not list1:
            return list2
        if not list2:
            return list1
        
        # convert and combine the 2 lists
        l = linkedlist_to_list(list1) + linkedlist_to_list(list2)
        
        # exit if comparison between elements will fail
        if any(not isinstance(element, (int, float)) for element in l):
            return None
        
        # sort the list and return the list represented as a linked list
        l.sort()
        return list_to_linkedlist(l)
    
    def mergeTwoLists_2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
            Merges two sorted linked lists into a single sorted linked list.

            This function takes two linked lists that are already sorted and merges them 
            into a new sorted linked list. It handles cases where one or both lists may 
            be empty and ensures that the values in the lists are integers.

            Args:
                list1 (Optional[ListNode]): The head of the first sorted linked list.
                list2 (Optional[ListNode]): The head of the second sorted linked list.

            Returns:
                Optional[ListNode]: The head of the merged sorted linked list. 
                Returns None if any of the nodes contain non-integer values.
        """
        # if the inputs are empty or None, return the other. (If both are not valid the first empty/None node will be returned)
        if not list1:
            return list2
        if not list2:
            return list1
        
        # create a dummy and head node to attach new nodes to, creating two prevents the possibility
        #   of attempting to get the value of None.next when node.next would be None
        dummy = head = ListNode()
        
        # the head will come before the attachment node
        head.next = dummy
        
        # while both lists have nodes
        while list1 and list2:
            
            # extract the values and verify that they can be compared, return None if they cant
            val1, val2 = list1.val, list2.val
            if not isinstance(val1, (int, float)) or not isinstance(val2, (int, float)):
                return None
            
            # if the value of the current node in list1 is lower than the value of the current node in list2,
            #   attach the current list1 node to the dummy and update the position in list1 to the next node
            if val1 < val2:
                dummy.next = list1
                list1 = list1.next
            # if the value of the current node in list2 is greater than or equal to the value of the current node in list1,
            #   attach the current list2 node to the dummy and update the position in list2 to the next node
            else:
                dummy.next = list2
                list2 = list2.next
            
            # update the dummy node to accept a new node on the next loop iteration
            dummy = dummy.next
            
        # if either list still has nodes, append them to the end of the linked list
        if list1:
            dummy.next = list1
        if list2:
            dummy.next = list2
        
        # return the first node of the modified list (dummy is at the end of the list, so head.next is the correct first node)
        return head.next
    
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
    "list1, list2, expected",
    [
        # Happy path tests
        pytest.param(list_to_linkedlist([1, 2, 4]), list_to_linkedlist([1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        pytest.param(list_to_linkedlist([1, 3, 5]), list_to_linkedlist([2, 4, 6]), [1, 2, 3, 4, 5, 6]),
        
        # Edge cases
        pytest.param(None, list_to_linkedlist([1, 2, 3]), [1, 2, 3]),
        pytest.param(list_to_linkedlist([1, 2, 3]), None, [1, 2, 3]),
        pytest.param(None, None, []),
        pytest.param(list_to_linkedlist([]), list_to_linkedlist([]), []),
        pytest.param(list_to_linkedlist([]), list_to_linkedlist([1, 2, 3]), [1, 2, 3]),
        pytest.param(list_to_linkedlist([1, 2, 3]), list_to_linkedlist([]), [1, 2, 3]),
        
        # Error cases
        pytest.param(list_to_linkedlist([1, 2, 3]), list_to_linkedlist([1, 2, 'a']), None), # type: ignore
    ],
    ids = [
        "happy_path_1", "happy_path_2", "edge_case_list1_none",
        "edge_case_list2_none", "edge_case_both_none", "edge_case_both_empty",
        "edge_case_list1_empty", "edge_case_list2_empty", "error_case_invalid_data_type"
    ]
)
def test_mergeTwoLists(list1, list2, expected):
    
    # Act
    result = Solution().mergeTwoLists_2(list1, list2)
    
    # Assert
    if expected is None:
        assert result is None
    else:
        assert linkedlist_to_list(result) == expected
        
if __name__ == "__main__":
    print(linkedlist_to_list(Solution().test()))
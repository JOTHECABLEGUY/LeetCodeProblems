"""108. Convert Sorted Array to Binary Search Tree
Easy
Topics
Companies
Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
binary search tree.

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order."""

import pytest
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    
    def test(self):
        return self.sortedArrayToBST([1, 2, 3, 4, 5, 6, 7])
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
            Converts a sorted array into a height-balanced binary search tree.

            This function takes a sorted list of integers and recursively constructs a binary search tree (BST) 
            such that the tree is height-balanced. The middle element of the array becomes the root, and the left 
            and right subarrays are used to create the left and right subtrees, respectively.

            Args:
                nums (List[int]): A sorted list of integers to be converted into a binary search tree.

            Returns:
                Optional[TreeNode]: The root node of the constructed height-balanced binary search tree, 
                                    or None if the input list is empty.
        """
        
        # if the input array is empty or None, return None
        if not nums:
            return None
        
        # if there is only 1 element, return the single element as a node
        if len(nums) == 1:
            return TreeNode(nums[0])
        
        # create a new root using the middle of the list
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        
        # get the subtrees on each side of the new root, dividing the input list further
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        # return the root once each subtree is complete, completing each recursive call 
        #   until the first, which returns the root of the whole tree
        return root

def inorder(tree: Optional[TreeNode]) -> List[int]:
    """
    Method to traverse a Tree in 'inorder' order , left subtree -> root -> right subtree 
    (i.e sorted from smallest to highest)

    Args:
        tree (Optional[TreeNode]): tree to traverse, or None

    Returns:
        List[int]: list of integers representing the input tree in the above mentioned order, can be empty
                    if a null tree was provided
    """
    return inorder(tree.left) + [tree.val] + inorder(tree.right) if tree else []

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([1, 2, 3], TreeNode(2, TreeNode(1), TreeNode(3))),  # simple case
        ([1, 2, 3, 4, 5, 6, 7], TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))),  # larger case

        # Edge cases
        ([], None),  # empty list
        ([1], TreeNode(1)),  # single element
        ([1, 2], TreeNode(2, TreeNode(1))),  # two elements

        # Error cases
        (None, None),  # None input
    ],
    ids=[
        "simple_case",
        "larger_case",
        "empty_list",
        "single_element",
        "two_elements",
        "none_input",
    ]
)
def test_sortedArrayToBST(nums, expected):
    # Act
    result = Solution().sortedArrayToBST(nums)

    # Assert
    assert inorder(result) == inorder(expected)

if __name__ == "__main__":
    res = Solution().test()
    if res is not None:
        print(inorder(res))
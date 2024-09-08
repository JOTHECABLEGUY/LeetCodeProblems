"""35. Search Insert Position
Easy
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.searchInsert([1, 3, 5, 6], 7) # returns 4
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
            Searches for the index at which a target value should be inserted into a sorted list.

            This function performs a binary search to find the appropriate index for the target value in the given sorted list. 
            If the target is found, its index is returned; otherwise, the index where it can be inserted while maintaining order is returned.

            Args:
                nums (List[int]): A sorted list of integers in which to search for the target.
                target (int): The integer value to search for in the list.

            Returns:
                int: The index at which the target value is found or should be inserted.

            Raises:
                TypeError: If nums is not a list or if target is not an integer.
        """
        
        # raise TypeError if the  input types are incompatible
        if not isinstance(nums, list) or not isinstance(target, int):
            raise TypeError
        
        # if an empty list was passed in, return index of 0
        if not nums:
            return 0

        # helper function to perform binary search
        def bin_search(start:int, stop:int):
            """
                Performs a binary search to find the index of a target value in a sorted list.

                This recursive function checks the specified range of indices in the list to determine the position of the target value. 
                It returns the index of the target if found, or the index where the target should be inserted to maintain sorted order.

                Args:
                    start (int): The starting index of the range to search within the list.
                    stop (int): The ending index of the range to search within the list.

                Returns:
                    int: The index of the target value if found, or the index where it can be inserted.
            """
            
            # if window size reaches one (base case)
            if stop-start == 1:
                
                # other wise check where the value would fall and return the boundary depending on the value available
                return stop if target > nums[start] else start
            
            # when the base case is not met, the new middle point is the halfway point between the boundaries of the window
            mid = start + (stop-start)//2
            
            # if the new midpoint is the location of the target, return it
            if nums[mid] == target:
                return mid
            
            # depending on where target should be, recursively search either to the left or right of the mid point
            return bin_search(mid, stop) if target > nums[mid] else bin_search(0, mid)

        # search for the value within the whole list
        return bin_search(0, len(nums))

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Happy path tests
        ([1, 3, 5, 6], 5, 2),  # target is in the list
        ([1, 3, 5, 6], 2, 1),  # target is not in the list, should be inserted at index 1
        ([1, 3, 5, 6], 7, 4),  # target is greater than all elements, should be inserted at the end
        ([1, 3, 5, 6], 0, 0),  # target is less than all elements, should be inserted at the start

        # Edge cases
        ([], 1, 0),  # empty list, target should be inserted at index 0
        ([1], 0, 0),  # single element list, target less than element
        ([1], 2, 1),  # single element list, target greater than element
        ([1, 3], 2, 1),  # two elements, target between elements
        ([1, 3], 3, 1),  # two elements, target is the second element
    ],
    ids=[
        "target_in_list",
        "target_not_in_list",
        "target_greater_than_all",
        "target_less_than_all",
        "empty_list",
        "single_element_less",
        "single_element_greater",
        "two_elements_between",
        "two_elements_equal",
    ]
)
def test_searchInsert(nums, target, expected):
    # Act
    result = Solution().searchInsert(nums, target)

    # Assert
    assert result == expected

# Error cases
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 6], 'a', TypeError),  # target is not an integer
        ('1234', 2, TypeError),  # nums is not a list
        ([1, 3, 5, 6], None, TypeError),  # target is None
        ],
    ids=[
        "target_not_integer",
        "nums_not_list",
        "target_none",
    ]
)
def test_searchInsert_Exception(nums, target, expected):
        with pytest.raises(expected):
            Solution().searchInsert(nums, target)
            
if __name__ == "__main__":
    print(Solution().test())
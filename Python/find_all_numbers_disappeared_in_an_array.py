"""448. Find All Numbers Disappeared in an Array
Easy
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space."""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.findDisappearedNumbers([1, 2, 3, 4, 5, 6, 6])
    
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
            Identify the numbers that are missing from a given list of integers.

            This function returns a list of integers that are expected to be in the range from 1 to the length of the input list but are not present in the list. If the input list is empty, it returns an empty list.

            Args:
                nums (List[int]): A list of integers where some numbers in the range from 1 to len(nums) may be missing.

            Returns:
                List[int]: A list of integers that are missing from the input list.
        """
        
        # numbers that should be in the list
        range_set = set(range(1, len(nums)+1))
        
        # numbers that are actually in the list
        nums_set = set(nums)
        
        # find missing numbers by performing set subtraction. If nums is empty, return nothing
        return list(range_set - nums_set) if nums else []

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([4,3,2,7,8,2,3,1], [5,6]),  # missing numbers in the middle
        ([1,1], [2]),  # missing number at the end
        ([2,2], [1]),  # missing number at the beginning
        ([1,2,3,4,5], []),  # no missing numbers

        # Edge cases
        ([], []),  # empty list
        ([1], []),  # single element, no missing numbers
        ([2], [1]),  # single element, missing number
        ([1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10], [11, 12, 13, 14, 15, 16, 17, 18, 19]),  # multiple duplicates
        ([10,9,8,7,6,5,4,3,2,1], []),  # reversed order, no missing numbers
    ],
    ids=[
        "missing_numbers_in_the_middle",
        "missing_number_at_the_end",
        "missing_number_at_the_beginning",
        "no_missing_numbers",
        "empty_list",
        "single_element_no_missing",
        "single_element_missing",
        "multiple_duplicates",
        "reversed_order_no_missing",
    ]
)
def test_findDisappearedNumbers(nums, expected):
    # Act
    result = Solution().findDisappearedNumbers(nums)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
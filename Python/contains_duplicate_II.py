"""219. Contains Duplicate II
Easy
Topics
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 3)
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
            Check if there are two indices in the list such that their values are equal and their indices 
            are at most k apart.

            This function determines if any value appears at least twice in the list with their indices 
            differing by no more than k. It returns True if such a pair exists, otherwise it returns False.

            Args:
                nums (List[int]): A list of integers to check for nearby duplicates.
                k (int): The maximum allowed index difference between duplicate values.

            Returns:
                bool: True if there are duplicates within the specified index range, otherwise False.
        """
        
        # check if inputs are valid, return False if they are invalid
        if not nums or len(nums) == 1 or k <= 0:
            return False
        
        # if there are k or fewer elements in the list, check the whole list for duplicates
        if k >= len(nums):
            return len(set(nums)) != len(nums)
        
        # table to store indices of the last occurrence of number
        table = {}
        
        # for each number, check if it has been seen. if it has been seen, then check the difference
        #   between the current index and the last index where the current number was seen. If the difference
        #   if below or equal to k, then we have found a duplicate, otherwise update the last seen index 
        for i, num in enumerate(nums):
            if num in table and i - table[num] <= k:
                return True
            table[num] = i
        
        # if duplicates were no found, return False
        return False

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Happy path tests
        ([1, 2, 3, 1], 3, True),  # duplicate within range
        ([1, 0, 1, 1], 1, True),  # multiple duplicates within range
        ([1, 2, 3, 4], 2, False),  # no duplicates

        # Edge cases
        ([], 1, False),  # empty list
        ([1], 1, False),  # single element
        ([99, 99], 2, True), # 2 elements
        ([1, 2, 3, 1, 2, 3], 2, False),  # duplicates but out of range
        ([1, 2, 3, 1, 2, 3], 3, True),  # duplicates within range

        # Error cases
        ([1, 2, 3, 1], 0, False),  # k is zero
        ([1, 2, 3, 1], -1, False),  # k is negative
    ],
    ids=[
        "duplicate_within_range",
        "multiple_duplicates_within_range",
        "no_duplicates",
        "empty_list",
        "single_element",
        "2 elements",
        "duplicates_out_of_range",
        "duplicates_within_range",
        "k_is_zero",
        "k_is_negative",
    ]
)
def test_containsNearbyDuplicate(nums, k, expected):

    # Act
    result = Solution().containsNearbyDuplicate(nums, k)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
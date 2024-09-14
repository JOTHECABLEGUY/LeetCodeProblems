"""2419. Longest Subarray With Maximum Bitwise AND
Medium
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.


Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.longestSubarray([1, 2, 3, 4, 4])
    
    def longestSubarray(self, nums: List[int]) -> int:
        """
            Find the length of the longest contiguous subarray containing the maximum value.

            This function takes a list of integers and determines the length of the longest
            subarray where all elements are equal to the maximum value found in the list. 
            If the list is empty, it returns 0.

            Args:
                nums (List[int]): A list of integers to evaluate.

            Returns:
                int: The length of the longest contiguous subarray of the maximum value.
        """
        # exit early if an empty list is given
        if not nums:
            return 0
        
        # get maximum value in the input list
        maximum_input_val = max(nums)
        
        # set global and local maximum counts
        global_max = 1
        local_max = 0
        
        # for each input number, check if it is the maximum in the input array
        for num in nums:
            
            # if it is the maximum value from the list, increment the local max and 
            #   set the global max to the max of the global and local maxima
            if num == maximum_input_val:
                local_max += 1
                global_max = max(global_max, local_max)
            
            # otherwise the continuous string of maximum values has broken, so set the local max to 0
            else:
                local_max = 0
        
        # return the length of the longest subarray of continuous maximum-in-the-array values
        return global_max

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([1, 2, 3, 3, 2, 2], 2),  # multiple max values
        ([1, 2, 3, 4, 4, 4, 3], 3),  # consecutive max values
        ([1, 1, 1, 1], 4),  # all elements are the same
        ([5, 1, 5, 5, 2, 5, 5, 5], 3),  # scattered max values

        # Edge cases
        ([1], 1),  # single element
        ([2, 2, 2, 2, 2], 5),  # all elements are the same and max
        ([1, 2, 3, 4, 5], 1),  # strictly increasing
        ([5, 4, 3, 2, 1], 1),  # strictly decreasing

        # Error cases
        ([], 0),  # empty list
    ],
    ids=[
        "multiple_max_values",
        "consecutive_max_values",
        "all_elements_same",
        "scattered_max_values",
        "single_element",
        "all_elements_same_and_max",
        "strictly_increasing",
        "strictly_decreasing",
        "empty_list",
    ]
)
def test_longestSubarray(nums, expected):
    # Act
    result = Solution().longestSubarray(nums)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
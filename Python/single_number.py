"""136. Single Number
Easy
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once."""

from collections import Counter, defaultdict
import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.singleNumber([1, 1, 2, 2, 3])
    
    def singleNumber(self, nums: List[int]) -> int:
        """
            Find the single number in a list where every other number appears twice.

            This function identifies the number that appears exactly once in the provided list of integers. 
            If no such number exists or the list is empty, it returns zero.

            Args:
                nums (List[int]): A list of integers where every number except one appears twice.

            Returns:
                int: The single number that appears once, or 0 if no such number exists.
        """
        
        # exit if the list is not valid
        if not nums:
            return 0
        
        # create a counter object for the numbers
        c = Counter(nums)
        
        # the least common element will be at the end of a list of the most common
        least_common = c.most_common()[-1]
        
        # if the counter's least common element has the required count of 1, we can 
        #   return the least common element, otherwise return 0
        return least_common[0] if least_common[1] == 1 else 0

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([2, 2, 1], 1),  # Single number is 1
        ([4, 1, 2, 1, 2], 4),  # Single number is 4
        ([1], 1),  # Single number is 1 in a single-element list

        # Edge cases
        ([0, 0, 0, 1], 1),  # Single number is 1 with multiple zeros
        ([1, 1, 2, 2, 3], 3),  # Single number is 3 at the end
        ([1, 2, 2, 3, 3], 1),  # Single number is 1 at the beginning

        # Error cases
        ([], 0),  # Empty list should return 0
        ([1, 1, 1, 1], 0),  # No single number, should return 0
    ],
    ids=[
        "single_number_1",
        "single_number_4",
        "single_element_list",
        "multiple_zeros",
        "single_number_at_end",
        "single_number_at_beginning",
        "empty_list",
        "no_single_number"
    ]
)
def test_singleNumber(nums, expected):
    # Act
    result = Solution().singleNumber(nums)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
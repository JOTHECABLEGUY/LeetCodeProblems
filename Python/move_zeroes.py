"""283. Move Zeroes
Easy
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        nums = [0, 0, 1, 2, 0, 3]
        self.moveZeroes(nums)
        return nums
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        if not any(nums) or all(nums):
            return
        n = len(nums)
        count = 0
        for index in range(n):
            while index < len(nums) and nums[index] == 0:
                count += 1
                nums.pop(index)
        nums.extend([0]*count)

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),  # mix of zeroes and non-zeroes
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),    # no zeroes
        ([0, 0, 1], [1, 0, 0]),                # zeroes at the start
        ([1, 0, 0], [1, 0, 0]),                # zeroes at the end

        # Edge cases
        ([], []),                              # empty list
        ([0], [0]),                            # single zero
        ([1], [1]),                            # single non-zero
        ([0, 0, 0, 0], [0, 0, 0, 0]),          # all zeroes
        ([1, 1, 1, 1], [1, 1, 1, 1]),          # all non-zeroes

        # Error cases
        # No error cases for this function as it does not raise exceptions
    ],
    ids=[
        "mix_zeroes_nonzeroes",
        "no_zeroes",
        "zeroes_at_start",
        "zeroes_at_end",
        "empty_list",
        "single_zero",
        "single_nonzero",
        "all_zeroes",
        "all_nonzeroes"
    ]
)
def test_moveZeroes(nums, expected):
    # Act
    Solution().moveZeroes(nums)

    # Assert
    assert nums == expected

if __name__ == "__main__":
    print(Solution().test())
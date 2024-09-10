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
            Move all zeroes in the list to the end while maintaining the order of non-zero elements.

            This function modifies the input list in-place by shifting all non-zero elements to the front 
            and filling the remaining positions with zeroes. It handles cases where the list is empty, 
            contains only zeroes, or contains no zeroes.

            Args:
                nums (List[int]): A list of integers that may contain zeroes.

            Returns:
                None: The function modifies the input list in-place and does not return a value.
        """

        # exit early if an empty list was given or the list is all zeroes or all non-zeroes
        if not nums:
            return
        if not any(nums) or all(nums):
            return
        
        # index to insert next non-zero
        last_non_zero_found_position = 0
        
        # for each number in the list, if it is not zero, move it to the insertion index and increment the index
        for num in nums:
            if num != 0:
                nums[last_non_zero_found_position] = num
                last_non_zero_found_position += 1
        
        # at the end of the loop, only thing left is to overwrite the non-zeroes at the end to 0s
        #   get the number of zeroes to insert using the length of the input list - the position where 
        #   the next non-zero would be inserted. Replace the end of the list with the required
        #   number of 0s using slicing
        num_zeroes = len(nums) - last_non_zero_found_position
        nums[last_non_zero_found_position:] = [0]*num_zeroes

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
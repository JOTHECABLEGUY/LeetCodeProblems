"""55. Jump Game
Medium
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105"""

import pytest
from typing import List

class Solution:
    
    def test(self): return self.canJump([0, 2, 0, 0])
    
    def canJump(self, nums: List[int]) -> bool:
        """
            Determine if you can reach the last index of the array from the first index.

            This function evaluates whether it is possible to jump to the last index of a list of non-negative integers,
            where each element represents the maximum jump length from that position. It returns True if the last index
            can be reached, and False otherwise.

            Args:
                nums (List[int]): A list of non-negative integers representing the maximum jump length at each position.

            Returns:
                bool: True if the last index can be reached, False otherwise.
        """
        
        # return early for trivial cases
        if len(nums) < 2: return True
        
        # track the max index that can be reached
        m = 0
        
        # final index threshold: for readability
        final_index = len(nums) - 1
        
        # loop through each index
        for i in range(final_index):
            
            # if we ever get to an index that is past the max reachable, return False
            if i > m: return False
            
            # update the max reachable if an index's jump allows us to go further
            if i + nums[i] > m:
                m = i + nums[i]
                
                # return true if the updated max reaches the end of the list
                if m >= final_index: return True
        
        # return False if the loop never returns True (we are only able to reach the n-2 index)
        return False

@pytest.mark.parametrize("nums, expected", [
    # Happy path tests
    ([2, 3, 1, 1, 4], True),  # can jump to the end
    ([3, 2, 1, 0, 4], False),  # cannot jump to the end
    ([0], True),  # single element, trivially true
    ([2, 0, 0], True),  # can jump to the end

    # Edge cases
    ([1, 2, 3], True),  # can jump to the end
    ([1, 0, 1, 0], False),  # cannot jump to the end
    ([2, 5, 0, 0], True),  # can jump to the end
    ([1, 1, 1, 1], True),  # can jump to the end
    ([0, 2, 3], False),  # cannot jump to the end
    ([1, 0, 0, 0], False),  # cannot jump to the end
], ids=[
    "can_jump_to_end",
    "cannot_jump_to_end",
    "single_element",
    "can_jump_with_zeros",
    "simple_jump",
    "cannot_jump_with_zeros",
    "can_jump_with_large_step",
    "simple_jump_all_ones",
    "cannot_jump_start_zero",
    "cannot_jump_all_zeros"
])
def test_canJump(nums, expected):
    # Act
    result = Solution().canJump(nums)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test()) # False
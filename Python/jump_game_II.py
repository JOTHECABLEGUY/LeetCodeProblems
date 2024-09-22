"""45. Jump Game II
Medium
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].


Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1]."""

import pytest
from typing import List

class Solution:
    def test(self): return (self.jump([2,1,1,1,1]), self.jump([2,3,1,1,4]), 
                            self.jump([2,3,0,1,4]), self.jump([10,9,8,7,6,5,4,3,2,1,1,0]),
                            self.jump([4,1,1,3,1,1,1]))
    
    def jump(self, nums: List[int]) -> int:
        m = 0
        index = 0
        jmps = 0
        best_option = 0
        m = index + nums[index]
        while index < len(nums) - 1:
            if m >= len(nums) - 1: return jmps+1
            for i in range(index+1, m+1):
                if i + nums[i] > m: 
                    best_option = nums[i]
                    index = i
                    m = i + nums[i]
            if not best_option:
                index = m
            best_option = 0
            jmps += 1
        return jmps

@pytest.mark.parametrize("nums, expected, _id", [
    # Happy path tests
    ([2, 3, 1, 1, 4], 2, "happy_path_1"),
    ([2, 3, 0, 1, 4], 2, "happy_path_2"),
    
    # Edge cases
    ([0], 0, "single_element"),
    ([1, 2], 1, "two_elements"),
    ([1, 1, 1, 1], 3, "all_ones"),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0], 1, "large_first_jump"),
    
    # Error cases
    ([], 0, "empty_list"),
    ([1], 0, "single_element_1"),
])
def test_jump(nums, expected, _id):
    # Act
    result = Solution().jump(nums)
    
    # Assert
    assert result == expected, f"failed on {_id}"

if __name__ == "__main__":
    print(Solution().test())
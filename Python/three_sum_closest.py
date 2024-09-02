"""16. 3Sum Closest
Medium
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104"""
import pytest
from sys import maxsize
from typing import List, Union
class Solution:
    def test(self):
        return self.threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
    def threeSumClosest(self, nums: List[int], target: int) -> Union[int,None]:
        nums.sort()
        closest_sum, diff, n = maxsize, maxsize, len(nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, n - 1
            while l < r and closest_sum != target:
                curr_sum = nums[i] + nums[l] + nums[r]
                d = abs(curr_sum-target)
                if not d:
                    return curr_sum
                if d < diff:
                    diff = d
                    closest_sum = curr_sum
                if curr_sum < target:
                    l += 1
                else:
                    r -= 1
        return closest_sum if closest_sum - maxsize else None
@pytest.mark.parametrize(
"nums, target, expected",
[
    # Happy path tests
    ([1, 2, 3, 4], 6, 6),  # ID: happy_path_1
    ([-1, 2, 1, -4], 1, 2),  # ID: happy_path_2
    ([0, 0, 0], 1, 0),  # ID: happy_path_3

    # Edge cases
    ([1, 1, 1, 1], 3, 3),  # ID: edge_case_1
    ([1, 1, 1, 1], 4, 3),  # ID: edge_case_2
    ([1, 1, 1, 1], 5, 3),  # ID: edge_case_3

    # Error cases
    ([], 1, None),  # ID: error_case_1
    ([1], 1, None),  # ID: error_case_2
    ([1, 2], 1, None),  # ID: error_case_3
],
ids = ["happy_path_1", "happy_path_2", "happy_path_3", "edge_case_1", "edge_case_2",
       "edge_case_3", "error_case_1", "error_case_2", "error_case_3"]
)
def test_threeSumClosest(nums, target, expected):
    # Act
    result = Solution().threeSumClosest(nums, target)

    # Assert
    assert result == expected
    
if __name__ == "__main__":
    print(Solution().test())
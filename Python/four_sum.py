"""18. 4Sum
Medium
Topics
Companies
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109"""
import pytest
from typing import List
class Solution:
    def test(self):
        return self.fourSum([0,0,0,0], 0)
    def two_sum(self, start, nums, target):
        out = []
        l, r = start, len(nums) - 1
        while l < r:
            total = nums[l] + nums[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                out.append([nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while r < len(nums)-1 and l < r and nums[r] == nums[r+1]:
                    r -= 1
        return out
    def k_sum(self, start, nums, k, target, output, curr_klet):
        avg= target //k
        if start < len(nums) and nums[start] > avg or nums[-1] < avg:
            return
        if k < 2:
            return []
        if k == len(nums) and sum(nums) == target:
            output.append(nums)
            return
        if k == 2:
            for pair in self.two_sum(start, nums, target):
                output.append(curr_klet + pair)
        else:
            for i in range(start, len(nums)-k + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr_klet.append(nums[i])
                self.k_sum(i+1, nums, k-1, target-nums[i], output, curr_klet)
                curr_klet.pop()
        return
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        k, output, curr_klet = 4, [], []
        self.k_sum(0, nums, k, target, output, curr_klet)
                        
        return output

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Happy path tests
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        
        # Edge cases
        ([], 0, []),
        ([1, 2, 3, 4], 11, []),
        ([1, 1, 1, 1, 1, 1], 4, [[1, 1, 1, 1]]),
        
        # Error cases
        ([1, 2, 3], 6, []),  # Less than 4 elements
        ([1, 2, 3, 4, 5], 50, []),  # No possible quadruplet
    ],
    ids=[
        "happy_path_1",
        "happy_path_2",
        "edge_case_empty_list",
        "edge_case_no_quadruplet",
        "edge_case_all_same_elements",
        "error_case_less_than_4_elements",
        "error_case_no_possible_quadruplet",
    ]
)
def test_fourSum(nums, target, expected):
    # Act
    result = Solution().fourSum(nums, target)
    
    e_sets = {frozenset(e) for e in expected}
    r_sets = {frozenset(r) for r in result}
    
    # Assert
    assert e_sets == r_sets
if __name__ == "__main__":
    print(Solution().test())
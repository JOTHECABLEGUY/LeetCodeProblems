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
        return self.fourSum([1,-2,-5,-4,-3,3,3,5], -11)
    def check_inner_window(self, start, start_2, nums, target, res_set):
        r = len(nums)-1
        l = start_2 + 1
        quads = []
        while l < r:
            if nums[r] < 0 and target > 0:
                l = r
                continue
            quad = [nums[start], nums[start_2], nums[l], nums[r]]
            total = sum(quad)
            print(start, start_2, l, r, quad, total)
            if total == target:
                if set(quad) in res_set:
                    l += 1
                    continue
                res_set.append(set(quad))
                quads.append(quad)
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r-1] == nums[r]:
                    r-=1
            if total < target:
                l += 1
            if total > target:
                r -= 1
        return quads
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if not (n := len(nums)):
            return []
        if nums[-1] < 0 and target > 0:
            return []
        res = []
        res_set = []
        for start in range(n-3):
            if nums[start] > 0 and target - nums[start] < 0:
                return res
            if start > 0 and nums[start] == nums[start-1]:
                continue
            for start_2 in range(start+1, n-2):
                quads = self.check_inner_window(start, start_2, nums, target, res_set)
                res.extend(quads)
                        
        return res

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
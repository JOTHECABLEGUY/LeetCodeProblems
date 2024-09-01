"""15. 3Sum
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""
from typing import List
import pytest
class Solution:
    def test(self):
        return self.threeSum([-1,0,1,2,-1,-4])
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # cache_2 = {}
        freq_map = {num: nums.count(num) for num in nums}
        num_set = set(nums)
        res = []
        res_set = []
        for index, i in enumerate(nums):
            for j in nums[index+1:]:
                s = (i + j) * -1
                if s in num_set:
                    r = [s] + [i, j]
                    r_set = set(r)
                    if r.count(s) <= freq_map[s] and r_set not in res_set:
                        res.append(r)
                        res_set.append(r_set)
        return res
@pytest.mark.parametrize("nums, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),  # ID: happy_path_1
    ([], []),  # ID: happy_path_2
    ([0], []),  # ID: happy_path_3
    # Edge cases
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),  # ID: edge_case_1
    ([0, 0, 0], [[0, 0, 0]]),  # ID: edge_case_2
    # Error cases
    ([1, 2, -2, -1], []),  # ID: error_case_1
    ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),  # ID: error_case_2
],
    ids = ["happy_path_1", "happy_path_2", "happy_path_3", "edge_case_1", "edge_case_2", "error_case_1", "error_case_2"])
def test_all(nums, expected):
    result = Solution().threeSum(nums)
    r_sets = [set(r) for r in result]
    e_sets = [set(e) for e in expected]
    assert all(r in e_sets for r in r_sets)
if __name__ == "__main__":
    print(Solution().test())
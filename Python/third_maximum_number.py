"""414. Third Maximum Number
Easy
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1. 

Constraints:

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Can you find an O(n) solution?"""

import heapq
from queue import PriorityQueue
import pytest
from typing import List

class Solution:
    def test(self):
        return self.thirdMax([1, 2, 3])
    def thirdMax(self, nums: List[int]) -> int:
        n = sorted(list(set(nums)))
        return n[-3] if len(n) >= 3 else n[-1]

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([3, 2, 1], 1),
        ([1, 2], 2),
        ([2, 2, 3, 1], 1),
        ([1, 2, 3, 4, 5], 3),
        
        # Edge cases
        ([1, 1, 1], 1),
        ([1, 2, 2, 3], 1),
        ([1, 2, 3], 1),
        ([5, 4, 3, 2, 1], 3),
        
        # Error cases
        ([1], 1),
        ([1, 1], 1),
    ],
    ids=[
        "three_distinct_numbers", "two_numbers", "duplicates_in_list", "more_than_three_numbers", "all_elements_same", 
        "duplicates_with_three_distinct", "exactly_three_numbers", "descending_order", "single_element", "two_same_elements"
        ]
)
def test_thirdMax(nums, expected):
    # Act
    result = Solution().thirdMax(nums)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
"""219. Contains Duplicate II
Easy
Topics
Companies
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.


Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 3)
    
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) == 1 or k <= 0:
            return False
        if k >= len(nums):
            return len(set(nums)) != len(nums)
        r = k +1
        prev_seq = nums[:r]
        if len(set(prev_seq)) != k+1:
            return True
        while r < len(nums):
            prev_seq.pop(0)
            prev_seq.append(nums[r])
            if len(set(prev_seq)) != k+1:
                return True
            r+=1
        return False

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Happy path tests
        ([1, 2, 3, 1], 3, True),  # duplicate within range
        ([1, 0, 1, 1], 1, True),  # multiple duplicates within range
        ([1, 2, 3, 4], 2, False),  # no duplicates

        # Edge cases
        ([], 1, False),  # empty list
        ([1], 1, False),  # single element
        ([99, 99], 2, True), # 2 elements
        ([1, 2, 3, 1, 2, 3], 2, False),  # duplicates but out of range
        ([1, 2, 3, 1, 2, 3], 3, True),  # duplicates within range

        # Error cases
        ([1, 2, 3, 1], 0, False),  # k is zero
        ([1, 2, 3, 1], -1, False),  # k is negative
    ],
    ids=[
        "duplicate_within_range",
        "multiple_duplicates_within_range",
        "no_duplicates",
        "empty_list",
        "single_element",
        "2 elements",
        "duplicates_out_of_range",
        "duplicates_within_range",
        "k_is_zero",
        "k_is_negative",
    ]
)
def test_containsNearbyDuplicate(nums, k, expected):

    # Act
    result = Solution().containsNearbyDuplicate(nums, k)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
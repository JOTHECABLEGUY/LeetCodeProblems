"""169. Majority Element
Easy
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?"""

import pytest
from collections import Counter, defaultdict
from typing import List
class Solution:
    
    def test(self):
        return self.majorityElement([2, 2, 1, 1, 1, 2, 2])
    
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        c = Counter(nums)
        mc = c.most_common(1)[0]
        return mc[0] if mc[1] > len(nums)//2 else 0
    
    def majorityElement_2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = defaultdict(int)
        half = len(nums)//2 
        for num in nums:
            m[num] += 1
            if m[num] > half:
                return num
        return 0
                
    
@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        
        # Edge cases
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, 5], 0),
        ([1, 1, 1, 2, 2, 2, 2], 2),
        
        # Error cases
        ([1, 2, 3, 4, 5, 6], 0),
        ([1, 1, 2, 2, 3, 3], 0),
    ],
    ids=[
        "majority_element_present", "majority_element_present_longer_list", "empty_list", "single_element_list", 
        "no_majority_element", "majority_element_exactly_half_plus_one", "no_majority_element_even_length", "no_majority_element_tied_counts"
    ]
)
def test_majorityElement(nums, expected):
    # Act
    result = Solution().majorityElement_2(nums)
    
    # Assert
    assert result == expected
if __name__ == "__main__":
    print(Solution().test())
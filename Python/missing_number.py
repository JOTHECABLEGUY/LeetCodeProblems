"""268. Missing Number
Easy
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique."""

import pytest
from typing import List, Optional

class Solution:
    
    def test(self):
        return self.missingNumber([0, 1, 2, 3, 5])
    
    def missingNumber(self, nums: List[int]) -> Optional[int]:
        s = set(range(len(nums) + 1))
        if len(set(nums)) != len(nums) or (nums and max(nums) not in s):
            return None 
        for num in nums:
            s.remove(num)
        return s.pop()

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9,6,4,2,3,5,7,0,1], 8),
        
        # Edge cases
        ([0], 1),
        ([1], 0),
        ([], 0),
        
        # Error cases
        ([0, 0], None),
        ([1, 1], None),
        ([0, 3], None),
    ],
    ids=[
        "missing middle number", "missing last number", "missing number in large list", "single element zero", 
        "single element one", "empty list", "duplicate zero", "duplicate one", "missing multiple numbers"
    ]
)
def test_missingNumber(nums, expected):
    # Act
    result = Solution().missingNumber(nums)
    
    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
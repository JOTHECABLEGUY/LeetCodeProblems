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
        """
            Find the missing number in a list of integers from 0 to n.

            This function calculates the missing number in a sequence of integers that should 
            range from 0 to n, where one number is absent. It uses the formula for the sum of 
            the first n natural numbers to determine the missing value.

            Args:
                nums (List[int]): A list of integers containing n distinct numbers in the range [0, n].

            Returns:
                int: The missing number from the list.

        """

        # get numbers to sum
        n = len(nums)
        
        # check if there are duplicates or more than 1 missing value (more than 1 missing value is only caught when 
        #   the maximum value in the list is above the length of the list)
        if len(set(nums)) != len(nums) or (nums and max(nums) > n):
            return None
        
        # return sum of first n natural numbers minus the sum of the numbers provided
        return n*(n+1)//2 - sum(nums)

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
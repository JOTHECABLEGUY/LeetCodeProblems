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
        """
            Identify the majority element in a list of integers, if one exists.

            This function counts the occurrences of each number in the list and determines if any number 
            appears more than half the time. If such a majority element is found, it is returned; otherwise, 
            the function returns zero.

            Args:
                nums (List[int]): A list of integers where a majority element may exist.

            Returns:
                int: The majority element if it exists, otherwise 0.

        """

        # return if an invalid list was given
        if not nums:
            return 0
        
        # create counter over the input list
        c = Counter(nums)
        
        # get the most comm element
        mc = c.most_common(1)[0]
        
        # return the element if it appeared more than half of the time, else 0
        return mc[0] if mc[1] > len(nums)//2 else 0
    
    def majorityElement_2(self, nums: List[int]) -> int:
        """
            Find the majority element in a list of integers, if one exists.

            This function counts the occurrences of each number in the list and checks if any number appears 
            more than half the time. If such a majority element is found, it is returned; otherwise, the function 
            returns zero.

            Args:
                nums (List[int]): A list of integers where a majority element may exist.

            Returns:
                int: The majority element if it exists, otherwise 0.
        """
        
        # return if an invalid list was given
        if not nums:
            return 0
        
        # create a dictionary to track frequency of numbers
        m = defaultdict(int)
        
        # threshold to reach before returning
        half = len(nums)//2
        
        # check each number, if its frequency meets threshold, return it
        for num in nums:
            m[num] += 1
            if m[num] > half:
                return num
        
        # return 0 if no majority element was found
        return 0
    
    def majorityElement_3(self, nums: List[int]) -> int:
        """
            Determine the majority element in a list of integers, assuming one exists.

            This function finds the majority element by sorting the list and returning the element 
            at the middle index. It is based on the assumption that there is always a majority element present.

            Args:
                nums (List[int]): A list of integers where a majority element is guaranteed to exist.

            Returns:
                int: The majority element in the list.
        """
        
        # if an invalid input was given
        if not nums: return 0
        
        # sort the numbers
        nums.sort()
        
        # majority element will be in the middle
        return nums[len(nums)//2]
    
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
    result = Solution().majorityElement_3(nums)
    
    # Assert
    assert result == expected
    
if __name__ == "__main__":
    print(Solution().test())
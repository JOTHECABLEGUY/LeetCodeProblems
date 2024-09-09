"""217. Contains Duplicate
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109"""

from functools import reduce
from operator import xor
import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.containsDuplicate([1, 1, 2])
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
            Determine if a list contains any duplicate elements.

            This function checks if there are any numbers in the provided list that appear more than once. 
            It returns True if duplicates are found, and False if all elements are unique.

            Args:
                nums (List[int]): A list of integers to check for duplicates.

            Returns:
                bool: True if duplicates exist, otherwise False.
        """
        
        # set to hold already visited elements
        seen = set()
        
        # check if each number is in the set. If it is, return, otherwise add to the set and continue
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        
        # return False since the loop did not return True
        return False

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([1, 2, 3, 4], False),  # unique elements
        ([1, 2, 3, 1], True),   # duplicate elements
        ([1, 1, 1, 1], True),   # all elements the same

        # Edge cases
        ([], False),            # empty list
        ([1], False),           # single element
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),  # large list with unique elements
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], True), # large list with duplicates

        # Error cases
        ([1, 'a', 3, 4], False), # mixed types, assuming function handles it gracefully
    ],
    ids=[
        "unique_elements",
        "duplicate_elements",
        "all_elements_same",
        "empty_list",
        "single_element",
        "large_unique_list",
        "large_list_with_duplicates",
        "mixed_types"
    ]
)
def test_containsDuplicate(nums, expected):
    # Act
    result = Solution().containsDuplicate(nums)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
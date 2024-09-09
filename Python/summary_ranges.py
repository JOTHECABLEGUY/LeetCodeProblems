"""228. Summary Ranges
Easy
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order."""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.summaryRanges([1, 2, 3, 4, 6])
    
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
            Summarize a list of integers into a list of ranges.

            This function takes a sorted list of integers and groups consecutive numbers into ranges. 
            It returns a list of strings representing these ranges, where a range is formatted as 
            "start->end" for consecutive numbers, and single numbers are represented as themselves.

            Args:
                nums (List[int]): A list of sorted integers.

            Returns:
                List[str]: A list of strings representing the summarized ranges.

        """
        
        # return in empty list is provided
        if not nums:
            return []
        
        # list to hold range strings
        res = []
        
        # list to hold working ranges of numbers
        ranges = [[nums[0]]]
        
        # for each number after the first
        for i in range(1, len(nums)):
            
            # get the most recent range
            curr_range = ranges[-1]
            
            # check if the last number is 1 less than the current number (meaning this number is consecutive).
            #   If it is, add it to the range
            if nums[i] - 1 == curr_range[-1]:
                curr_range.append(nums[i])
                
            # otherwise, make a new range in the ranges list
            else:
                ranges.append([nums[i]])
        
        # for each range, make a string representing the list
        for r in ranges:
            
            # if there is one element, only put the number as a string
            if len(r) == 1:
                res.append(str(r[0]))
            
            # otherwise put the first and last elements of the list with an arrow between them
            else:
                res.append(f"{r[0]}->{r[-1]}")
        
        # return the list of ranges expressed as strings
        return res

@pytest.mark.parametrize(
    "nums, expected",
    [
        # Happy path tests
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ([1, 3, 5, 7], ["1", "3", "5", "7"]),

        # Edge cases
        ([], []),
        ([1], ["1"]),
        ([1, 2], ["1->2"]),
        ([1, 3], ["1", "3"]),

        # Error cases
        ([1, 1, 1], ["1", "1", "1"]),
        ([1, 2, 2, 3], ["1->2", "2->3"]),
    ],
    ids = [
        "happy_path_1", "happy_path_2", "happy_path_3", "empty_list", "single_element","two_elements_consecutive",
        "two_elements_non_consecutive", "duplicate_elements", "consecutive_duplicates"
    ]
)
def test_summaryRanges(nums, expected):
    # Act
    result = Solution().summaryRanges(nums)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
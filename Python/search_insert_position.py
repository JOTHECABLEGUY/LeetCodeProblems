"""35. Search Insert Position
Easy
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104"""

import pytest
from typing import List

class Solution:
    def test(self):
        return self.searchInsert([1, 3, 5, 6], 7)
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not isinstance(nums, list) or not isinstance(target, int):
            raise TypeError

        if not nums:
            return 0

        def bin_search(start, stop):
            if stop-start <= 1:
                if target == nums[start]:
                    return start
                if target == nums[stop-1]:
                    return stop
                return stop if target > nums[stop-1] else start
            mid = (start + stop)//2
            return bin_search(mid, stop) if target >= nums[mid] else bin_search(0, mid)

        return bin_search(0, len(nums))

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Happy path tests
        ([1, 3, 5, 6], 5, 2),  # target is in the list
        ([1, 3, 5, 6], 2, 1),  # target is not in the list, should be inserted at index 1
        ([1, 3, 5, 6], 7, 4),  # target is greater than all elements, should be inserted at the end
        ([1, 3, 5, 6], 0, 0),  # target is less than all elements, should be inserted at the start

        # Edge cases
        ([], 1, 0),  # empty list, target should be inserted at index 0
        ([1], 0, 0),  # single element list, target less than element
        ([1], 2, 1),  # single element list, target greater than element
        ([1, 3], 2, 1),  # two elements, target between elements
        ([1, 3], 3, 1),  # two elements, target is the second element
    ],
    ids=[
        "target_in_list",
        "target_not_in_list",
        "target_greater_than_all",
        "target_less_than_all",
        "empty_list",
        "single_element_less",
        "single_element_greater",
        "two_elements_between",
        "two_elements_equal",
    ]
)
def test_searchInsert(nums, target, expected):
    # Act
    result = Solution().searchInsert(nums, target)

    # Assert
    assert result == expected

# Error cases
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 6], 'a', TypeError),  # target is not an integer
        ('1234', 2, TypeError),  # nums is not a list
        ([1, 3, 5, 6], None, TypeError),  # target is None
        ],
    ids=[
        "target_not_integer",
        "nums_not_list",
        "target_none",
    ]
)
def test_searchInsert_Exception(nums, target, expected):
        with pytest.raises(expected):
            Solution().searchInsert(nums, target)
            
if __name__ == "__main__":
    print(Solution().test())
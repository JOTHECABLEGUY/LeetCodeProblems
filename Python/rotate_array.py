"""189. Rotate Array
Medium
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        nums = [1, 2, 3, 4]
        nums1 = nums.copy()
        k = 2
        self.rotate(nums, k)
        return (nums1, nums)
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        k %= len(nums)
        if not k: return
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # Happy path tests
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),  # rotate by 3
        ([1, 2, 3, 4, 5, 6, 7], 0, [1, 2, 3, 4, 5, 6, 7]),  # rotate by 0
        ([1, 2, 3, 4, 5, 6, 7], 7, [1, 2, 3, 4, 5, 6, 7]),  # rotate by length of array

        # Edge cases
        ([1], 1, [1]),  # single element array
        ([1, 2], 1, [2, 1]),  # two elements, rotate by 1
        ([1, 2, 3], 4, [3, 1, 2]),  # rotate by more than length of array

        # Error cases
        ([], 3, []),  # empty array
    ],
    ids=[
        "rotate_by_3",
        "rotate_by_0",
        "rotate_by_length",
        "single_element",
        "two_elements_rotate_by_1",
        "rotate_by_more_than_length",
        "empty_array",
    ]
)
def test_rotate(nums, k, expected):
    solution = Solution()

    # Act
    solution.rotate(nums, k)

    # Assert
    assert nums == expected

if __name__ == "__main__":
    print(Solution().test())
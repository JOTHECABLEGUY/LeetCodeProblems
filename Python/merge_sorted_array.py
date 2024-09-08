"""88. Merge Sorted Array
Easy
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?"""

import pytest
from typing import List
class Solution:
    def test(self):
        nums1 = [1, 2, 4, 5, 6, 0]
        nums2 = [2, 4, 6]
        n = len(nums2)
        m = len(nums1) - n
        self.merge(nums1, 5, [3], 1)
        return nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right = 0, 0
        res = []
        while left < m and right < n:
            if nums1[left] <= nums2[right]:
                res.append(nums1[left])
                left += 1
            else:
                res.append(nums2[right])
                right += 1
        if left < m:
            res.extend(nums1[left:m])
        elif right < n:
            res.extend(nums2[right:])
        nums1[:m+n] = res

@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        # Happy path tests
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 4, 5, 6, 0], 5, [3], 1, [1, 2, 3, 4, 5, 6]),
        
        # Edge cases
        ([0], 0, [1], 1, [1]),
        ([1], 1, [], 0, [1]),
        ([0, 0, 0], 0, [2, 5, 6], 3, [2, 5, 6]),
        ([1, 2, 3], 3, [], 0, [1, 2, 3]),
        
        # Error cases
        ([1, 2, 3], 3, [4, 5, 6], 0, [1, 2, 3]),
        ([0, 0, 0], 0, [1, 2, 3], 3, [1, 2, 3]),
    ],
    ids=[
        "happy_path_1",
        "happy_path_2",
        "happy_path_3",
        "edge_case_1",
        "edge_case_2",
        "edge_case_3",
        "edge_case_4",
        "error_case_1",
        "error_case_2",
    ]
)
def test_merge(nums1, m, nums2, n, expected):
    # Act
    Solution().merge(nums1, m, nums2, n)
    
    # Assert
    assert nums1 == expected

if __name__ == "__main__":
    print(Solution().test())
        
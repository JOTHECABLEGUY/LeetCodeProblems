"""350. Intersection of Two Arrays II
Easy
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?"""

import pytest
from typing import List
from collections import Counter

class Solution:
    
    def test(self):
        return self.intersect([1, 2, 3], [2, 3, 4, 3])
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        for num in set(nums1):
            count = min(c1.get(num, 0), c2.get(num, 0))
            if count > 0:
                res.extend([num]*count)
        return res

@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        # Happy path tests
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),
        ([1, 2, 3], [4, 5, 6], []),
        
        # Edge cases
        ([], [], []),
        ([1, 2, 3], [], []),
        ([], [1, 2, 3], []),
        ([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]),
        ([1, 2, 3], [3, 2, 1], [1, 2, 3]),
        
        # Error cases
        ([1, 2, 3], [None], []),
        ([None], [1, 2, 3], []),
        ([None], [None], [None]),
    ],
    ids=[
        "happy_path_1",
        "happy_path_2",
        "happy_path_3",
        "edge_case_empty_lists",
        "edge_case_nums2_empty",
        "edge_case_nums1_empty",
        "edge_case_all_duplicates",
        "edge_case_all_elements_intersect",
        "error_case_nums2_contains_none",
        "error_case_nums1_contains_none",
        "error_case_both_contain_none",
    ]
)
def test_intersect(nums1, nums2, expected):
    # Act
    result = Solution().intersect(nums1, nums2)

    # Assert
    assert sorted(result) == sorted(expected)

if __name__ == "__main__":
    print(Solution().test())
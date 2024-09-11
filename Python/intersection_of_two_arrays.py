"""349. Intersection of Two Arrays
Easy
Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.


Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000"""

import pytest
from typing import Optional, List

class Solution:
    
    def test(self):
        return self.intersection([1, 2, 3], [3, 4, 5])
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> Optional[List[int]]:
        """
            Compute the intersection of two integer lists.

            This method returns a list of unique integers that are present in both input lists. 
            If both lists are empty, it returns the first list.

            Args:
                nums1 (List[int]): The first list of integers.
                nums2 (List[int]): The second list of integers.

            Returns:
                Optional[List[int]]: A list of unique integers that are present in both lists, 
                or the first list if both are empty.
        """
        
        return nums1 if not nums1 and not nums2 else list(set(nums1) & set(nums2))

@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        # Happy path tests
        ([1, 2, 2, 1], [2, 2], [2]),  # common elements
        ([4, 9, 5], [9, 4, 9, 8, 4], [9, 4]),  # multiple common elements
        ([1, 2, 3], [4, 5, 6], []),  # no common elements

        # Edge cases
        ([], [1, 2, 3], []),  # first list empty
        ([1, 2, 3], [], []),  # second list empty
        ([], [], []),  # both lists empty
        ([1, 1, 1], [1, 1, 1], [1]),  # all elements the same

        # Error cases
        ([1, 2, 3], [None, 2, 3], [2, 3]),  # None in second list
        ([None, None], [None], [None]),  # None in both lists
    ],
    ids=[
        "common_elements",
        "multiple_common_elements",
        "no_common_elements",
        "first_list_empty",
        "second_list_empty",
        "both_lists_empty",
        "all_elements_same",
        "none_in_second_list",
        "none_in_both_lists",
    ]
)
def test_intersection(nums1, nums2, expected):
    # Act
    result = Solution().intersection(nums1, nums2)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
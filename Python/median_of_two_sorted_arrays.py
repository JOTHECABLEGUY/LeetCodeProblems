"""4. Median of Two Sorted Arrays
Hard
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106"""
from typing import List, Union
import pytest
class Solution:
    def test(self):
        return self.findMedianSortedArrays([1], [2,3,4,5])
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> Union[int, float,None]:
        if not nums1 and not nums2:
            return None
        overall_array = []
        overall_length = len(nums1) + len(nums2)
        median_index = overall_length//2
        target_length = median_index + 1
        if not overall_length % 2:
            median_index = slice(median_index-1, median_index+1, 1)
            target_length += 1
        if not nums1:
            return nums2[median_index] if overall_length % 2 else sum(nums2[median_index])/2 # type: ignore
        if not nums2:
            return nums1[median_index] if overall_length % 2 else sum(nums1[median_index])/2 # type: ignore
        r_element, l_element = 1,1
        while l_element and r_element:
            if not overall_array:
                r_element = nums1.pop(0)
                l_element = nums2.pop(0)
            if r_element >= l_element:
                overall_array.append(l_element)
                if not nums2:
                    overall_array.append(r_element)
                    break
                l_element = nums2.pop(0)
            else:
                overall_array.append(r_element)
                if not nums1:
                    overall_array.append(l_element)
                    break
                r_element = nums1.pop(0)
        if (num_to_add := len(overall_array)- target_length) < 0:
            if nums1:
                overall_array.extend(nums1[:abs(num_to_add)+1])
            else:
                overall_array.extend(nums2[:abs(num_to_add)+1])
        return overall_array[median_index] if overall_length % 2 else sum(overall_array[median_index])/2 #type: ignore
@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        # Happy path tests
        ([1, 3], [2], 2.0),  # Single element in nums2
        ([1, 2], [3, 4], 2.5),  # Even total number of elements
        ([0, 0], [0, 0], 0.0),  # All elements are zero
        ([], [1], 1.0),  # nums1 is empty
        ([2], [], 2.0),  # nums2 is empty

        # Edge cases
        ([1, 2], [1, 2, 3], 2.0),  # Overlapping elements
        ([1, 3], [2, 4, 5], 3.0),  # Different lengths
        ([1, 2, 3], [4, 5, 6], 3.5),  # No overlapping elements
        ([1], [2, 3, 4], 2.5), # uneven lengths with one having one element
        ([1], [1], 1.0),  # Single element in both arrays
        ([1, 2, 3, 4], [5, 6, 7, 8], 4.5),  # Larger arrays

        # Error cases
        ([], [], None),  # Both arrays are empty
    ],
    ids=[
        "single_element_in_nums2",
        "even_total_elements",
        "all_elements_zero",
        "nums1_empty",
        "nums2_empty",
        "overlapping_elements",
        "different_lengths",
        "no_overlapping_elements",
        "uneven_lengths_with_one_having_one_element",
        "single_element_in_both",
        "larger_arrays",
        "both_arrays_empty",
    ]
)
def test_all(nums1, nums2, expected):
    
    median = Solution().findMedianSortedArrays(nums1, nums2)
    assert median == expected

if __name__ == "__main__":
    print(Solution().test())
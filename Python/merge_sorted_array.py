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
        nums1 = [0]
        nums2 = [1]
        n = len(nums2)
        m = len(nums1) - n
        self.merge(nums1, m, nums2, n)
        return nums1
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
            Merges two sorted integer arrays into one sorted array in-place.

            This function takes two sorted arrays, nums1 and nums2, and merges them into nums1, which has enough space to hold the combined elements. 
            The function modifies nums1 directly, ensuring that the final result is a single sorted array.

            Args:
                nums1 (List[int]): The first sorted array, which has a size of m + n, where the last n elements are empty.
                m (int): The number of valid elements in nums1.
                nums2 (List[int]): The second sorted array with n elements.
                n (int): The number of valid elements in nums2.

            Returns:
                None: This function modifies nums1 in-place and does not return a value.
        """
        
        # pointers for current positions in nums1 and nums2, as well as current position to insert result of comparison
        left, right, insertion_point = m - 1, n - 1, m + n - 1
        
        # while there are elements to compare from both lists
        while left >= 0 and right >= 0:
            
            # if the number in nums2 is bigger or equal to the number in nums1, 
            #   add the nums2 number to the insertion point, decrement right pointer
            if nums2[right] >= nums1[left]:
                nums1[insertion_point] = nums2[right]
                right -= 1
            # if the number in nums1 is bigger than the number in nums2, 
            #   add the nums1 number to the insertion point, decrement left pointer
            else:
                nums1[insertion_point] = nums1[left]
                left -= 1
            
            # both branches insert a value at the rightmost index, so decrement boundary for next insertion
            insertion_point -= 1
        
        # if any values have not been processed in nums2, insert all values into the beginning of nums1
        #   no need to consider nums1 value as they are already present in the array in the proper
        #   order if nums2 gets exhausted before nums1
        if right >= 0:
            nums1[:insertion_point+1] = nums2[:right+1]

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
        
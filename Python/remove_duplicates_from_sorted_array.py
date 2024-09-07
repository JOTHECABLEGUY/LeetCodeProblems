"""26. Remove Duplicates from Sorted Array
Easy
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order."""

import pytest
from typing import List
class Solution:
    
    def test(self):
        return self.removeDuplicates([1, 1, 2])
    
    def removeDuplicates(self, nums: List[int]) -> int:
        """
            Removes duplicates from a sorted array in place and returns the number of unique elements.

            This function modifies the input list such that the first part of the list contains only unique elements, 
            and returns the count of these unique elements. The order of the unique elements is preserved.

            Args:
                nums (List[int]): The sorted list of integers from which duplicates will be removed.

            Returns:
                int: The number of unique elements in the modified list.
        """
        
        # exit early if the list is empty 
        if not nums:
            return 0
        
        # keep track of number of unique elements
        num_unique = 1
        
        # skip first number
        for i in range(1, len(nums)):
            
            # check that the current number and previous number are different
            #   if they are, replace the number at the num_unique pointer with a
            #   number at position i, this ensures that the first k elements will 
            #   be unique. Increment num_unique
            #   if they aren't, continue
            if nums[i] != nums[i-1]:
                nums[num_unique] = nums[i]
                num_unique += 1
            
        # At the end of the loop, nums will have been modified inplace with the first num_unique numbers being unique
        return num_unique
    
@pytest.mark.parametrize("nums, expected_length, expected_nums", [
    # Happy path tests
    ([1, 1, 2], 2, [1, 2]),  # unique elements
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),  # multiple duplicates

    # Edge cases
    ([], 0, []),  # empty list
    ([1], 1, [1]),  # single element list
    ([1, 1, 1, 1], 1, [1]),  # all elements are the same
], ids=[
    "unique_elements",
    "multiple_duplicates",
    "empty_list",
    "single_element",
    "all_elements_same"
])
def test_removeDuplicates(nums, expected_length, expected_nums):
    # Act
    result_length = Solution().removeDuplicates(nums)

    # Assert
    assert result_length == expected_length
    assert nums[:result_length] == expected_nums
    
if __name__ == "__main__":
    print(Solution().test())
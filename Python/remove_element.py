"""27. Remove Element
Easy
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.


Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.removeElement([1, 2, 3], 3)
    
    def removeElement(self, nums: List[int], val: int) -> int:
        """
            Removes all instances of a specified value from a list in place and returns the count of remaining elements.

            This function iterates through the list, shifting non-target elements to the front while maintaining their order. 
            The function modifies the input list directly and returns the number of elements that are not equal to the specified value.

            Args:
                nums (List[int]): The list of integers from which to remove the specified value.
                val (int): The value to be removed from the list.

            Returns:
                int: The count of elements in the modified list that are not equal to the specified value.
        """
        
        # pointer to get index of next index to replace (also number of non-val characters)
        num_non_val = 0
        
        altered = False
        
        # check each element of the list
        for i in range(len(nums)):
            
            # if the value is not k, place it at the leftmost spot that has not been overwritten
            if nums[i] != val:
                
                # if there has been an instance of val seen, then we need to overwrite, otherwise skip over it
                if altered:
                    nums[num_non_val] = nums[i]
                
                # increment number of non val characters
                num_non_val += 1
            
            # if found an instance of val, overwriting will have to occur
            elif not altered:
                altered = True
        
        # return the number of non val numbers
        return num_non_val
    
@pytest.mark.parametrize(
    "nums, val, expected, description",
    [
        ([3, 2, 2, 3], 3, 2, "happy path with multiple occurrences of val"),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, "happy path with multiple occurrences of val and other elements"),
        ([1, 2, 3, 4, 5], 6, 5, "val not present in the list"),
        ([], 1, 0, "empty list"),
        ([1, 1, 1, 1], 1, 0, "all elements are val"),
        ([1, 2, 3, 4, 5], 1, 4, "val is the first element"),
        ([1, 2, 3, 4, 5], 5, 4, "val is the last element"),
        ([1], 1, 0, "single element list where element is val"),
        ([1], 2, 1, "single element list where element is not val"),
    ],
    ids=[
        "multiple_occurrences",
        "mixed_elements",
        "val_not_present",
        "empty_list",
        "all_elements_are_val",
        "val_first_element",
        "val_last_element",
        "single_element_is_val",
        "single_element_not_val",
    ]
)
def test_remove_element(nums, val, expected, description):
    # Act
    result = Solution().removeElement(nums, val)

    # Assert
    assert result == expected, f"Failed on: {description}"

if __name__ == "__main__":
    print(Solution().test())
"""18. 4Sum
Medium
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109"""
import pytest
from typing import List
class Solution:
    
    def test(self):
        return self.fourSum([0,0,0,0], 0)
    
    def two_sum(self, start:int, nums:List[int], target:int) -> List[List[int]]:
        """
            Returns zero or more pairs of numbers in the given array such that each pair sums up
            to the given target number.

        Args:
            start (int): the left-most index of the window to search for pairs
            nums (List[int]): the list of numbers to search
            target (int): the number that each returned pair must sum to

        Returns:
            List[List[int]]: a list of pairs that sum to the target number
        """
        # output array, left and right pointers
        out, l, r = [], start, len(nums) - 1 
        
        # loop until the 2 pointers meet
        while l < r:
            
            # sum the pair
            total = nums[l] + nums[r]
            
            # if the sum is below target, increase the sum of the pair by incrementing left pointer
            if total < target:
                l += 1
            
            # if the sum is above target, decrease the sum of the pair by decrementing right pointer
            elif total > target:
                r -= 1
            
            # if the pair sums to the target
            else:
                
                # add the pair to the output
                out.append([nums[l], nums[r]])
                
                # move the window in from both sides (if only one is changed, 
                # the sum cannot be equal to target without duplicating the pair)
                l += 1
                r -= 1
                
                # skip over any duplicates from the right and left
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while r < len(nums)-1 and l < r and nums[r] == nums[r+1]:
                    r -= 1
        
        # return the pairs that were captured during the search
        return out

    def k_sum(self, start: int, nums: List[int], k: int, target: int, output: List[List[int]], curr_klet: List[int]) -> None:
        """
        Adds the possible combinations of numbers with length k such that each number is not found at the 
        index of any other number in the combination and each combination sums up to target without 
        any duplicate combinations to the given output list.

        Args:
            start (int): starting index to start searching for combinations
            nums (List[int]): list of numbers to search
            k (int): required length of all combinations output
            target (int): number that each combination must sum to
            output (List[List[int]]): list of combinations that match the criteria above
            curr_klet (List[int]): list of numbers that are fixed. Each loop will have different fixed numbers
                                    such that the base case will provide the last 2 numbers for each combination
        """
        
        # if the first number in the search window is higher than the average, then there is no way
        #   for any remaining numbers to decrease the sum to target. Similarly, there is no way to
        #   increase the sum if the last number is below the average value required for each number
        #   in a valid combination
        avg = target // k
        if start < len(nums) and nums[start] > avg or nums[-1] < avg:
            return

        # if the each combination should be 1 or 0, no processing should be done
        if k < 2:
            return

        # if there are only k numbers in the array, check the sum, add the combination to the output
        #   if it reaches the target, and immediately return
        if k == len(nums) and sum(nums) == target:
            output.append(nums)
            return

        # base case, get all pairs in the window for current combination of length k-2
        if k == 2:
            output.extend(curr_klet + pair for pair in self.two_sum(start, nums, target))
            return
        
        # loop through the list, starting at 0 until there are k numbers left (cant make a combination with fewer than k nums)
        for i in range(start, len(nums)-k + 1):
            
            # if the current start point is not the first position, skip duplicate starting points.
            #   The first number will have made a combination using the duplicates if they were valid
            if i > start and nums[i] == nums[i-1]:
                continue
            
            # add the current number to the combination being built
            curr_klet.append(nums[i])
            
            # build off of the current combination by recursively checking for combinations of length
            #   k-1 such that the combinations added to the current number sum to the target
            self.k_sum(i+1, nums, k-1, target-nums[i], output, curr_klet)
            
            # need to pop the number we just processed, as any combinations using the previous value were
            #   already added to the output list
            curr_klet.pop()
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # sort the numbers in ascending order to allow for assumptions to be made during runtime
        nums.sort()
        
        # set up variables to hold the final list of combinations, the current base for combinations being built, 
        #   and the length that all valid combinations must be
        k, output, curr_klet = 4, [], []
        
        # build the combinations and add them to the output list
        self.k_sum(0, nums, k, target, output, curr_klet)
        
        # return the output list
        return output

@pytest.mark.parametrize(
    "nums, target, expected",
    [
        # Happy path tests
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        
        # Edge cases
        ([], 0, []),
        ([1, 2, 3, 4], 10, [[1, 2, 3, 4]]),
        ([1, 1, 1, 1, 1, 1], 4, [[1, 1, 1, 1]]),
        
        # Error cases
        ([1, 2, 3], 6, []),  # Less than 4 elements
        ([1, 2, 3, 4, 5], 50, []),  # No possible quadruplet
    ],
    ids=[
        "happy_path_1",
        "happy_path_2",
        "edge_case_empty_list",
        "edge_case_no_quadruplet",
        "edge_case_all_same_elements",
        "error_case_less_than_4_elements",
        "error_case_no_possible_quadruplet",
    ]
)
def test_fourSum(nums, target, expected):
    # Act
    result = Solution().fourSum(nums, target)
    
    e_sets = {frozenset(e) for e in expected}
    r_sets = {frozenset(r) for r in result}
    
    # Assert
    assert e_sets == r_sets
    
if __name__ == "__main__":
    print(Solution().test())
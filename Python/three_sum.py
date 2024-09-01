"""15. 3Sum
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105"""
from typing import List
import pytest
class Solution:
    def test(self):
        nums, expected = [82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324,1202,-90885,-2989,-95597,-34333,35528,5680,89093,-90606,50360,-29393,-27012,53313,65213,99818,-82405,-41661,-3333,-51952,72135,-1523,26377,74685,96992,92263,15929,5467,-99555,-43348,-41689,-60383,-3990,32165,65265,-72973,-58372,12741,-48568,-46596,72419,-1859,34153,62937,81310,-61823,-96770,-54944,8845,-91184,24208,-29078,31495,65258,14198,85395,70506,-40908,56740,-12228,-40072,32429,93001,68445,-73927,25731,-91859,-24150,10093,-60271,-81683,-18126,51055,48189,-6468,25057,81194,-58628,74042,66158,-14452,-49851,-43667,11092,39189,-17025,-79173,13606,83172,92647,-59741,19343,-26644,-57607,82908,-20655,1637,80060,98994,39331,-31274,-61523,91225,-72953,13211,-75116,-98421,-41571,-69074,99587,39345,42151,-2460,98236,15690,-52507,-95803,-48935,-46492,-45606,-79254,-99851,52533,73486,39948,-7240,71815,-585,-96252,90990,-93815,93340,-71848,58733,-14859,-83082,-75794,-82082,-24871,-15206,91207,-56469,-93618,67131], [[-95597, -3990, 99587], [-56469, -6468, 62937], [-49851, -20655, 70506], [-41689, -40908, 82597]]
        return self.threeSum(nums)

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            Finds all unique triplets in the list that sum to zero.

            This function takes a list of integers and returns a list of unique triplets 
            such that the sum of each triplet is equal to zero. It sorts the input list 
            and uses a two-pointer technique to efficiently find the triplets while avoiding duplicates.

            Args:
                nums (List[int]): A list of integers to evaluate for triplets.

            Returns:
                List[List[int]]: A list of unique triplets that sum to zero. 
                If no such triplets exist, an empty list is returned.
        """
        # sort the array so it is easier to allow some assumptions (such as if the current element > 0, break)
        nums.sort()
        n = len(nums)
        res = []
        
        # loop through the numbers list, keeping track of index
        for i, num in enumerate(nums):
            
            # if nums[i] > 0, then no triplet will ever be 0 (need a negative number or multiple 0s)
            # if i > n-2, then no triplet can be made as there will not be 3 numbers left
            if nums[i] > 0 or i > n - 2:
                break
            
            # skip over duplicate starting points
            if i > 0 and num == nums[i-1]:
                continue
            
            # initialize 2 pointers: 1 for the left and 1 for the right, so the indices will be i, l, r
            l = i + 1
            r = n - 1
            
            # stop looping when the 2 pointers meet
            while l < r:
                
                # get the total of the current triplet
                total = num + nums[l] + nums[r]
                
                # if the triplet sums to above 0, need to decrease the value of the triplet, which is achieved by decrementing the right index
                if total > 0:
                    r -= 1
                    
                # if the triplet sums to below 0, increment left pointer to increase the sum of the triplet
                elif total < 0:
                    l += 1
                    
                # if the triplet sums to 0, we have a valid entry. Add it to the result list
                else:
                    triplet = [num, nums[l], nums[r]]
                    res.append(triplet)
                    
                    # skip over duplicates from the left by incrementing left pointer if the left value is the same as what is in the current triplet
                    while l < r and nums[l] == triplet[1]:
                        l += 1
                    
                    # skip over duplicates from the right by decrementing right pointer if the right value is the same as what is in the current triplet
                    while l < r and nums[r] == triplet[2]:
                        r -= 1
        return res
@pytest.mark.parametrize("nums, expected", [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),  # ID: happy_path_1
    ([], []),  # ID: happy_path_2
    ([0], []),  # ID: happy_path_3
    # Edge cases
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),  # ID: edge_case_1
    ([0, 0, 0], [[0, 0, 0]]),  # ID: edge_case_2
    # Error cases
    ([1, 2, -2, -1], []),  # ID: error_case_1
    ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),  # ID: error_case_2
    ([82597,-9243,62390,83030,-97960,-26521,-61011,83390,-38677,12333,75987,46091,83794,19355,-71037,-6242,-28801,324,1202,-90885,-2989,-95597,-34333,35528,5680,89093,-90606,50360,-29393,-27012,53313,65213,99818,-82405,-41661,-3333,-51952,72135,-1523,26377,74685,96992,92263,15929,5467,-99555,-43348,-41689,-60383,-3990,32165,65265,-72973,-58372,12741,-48568,-46596,72419,-1859,34153,62937,81310,-61823,-96770,-54944,8845,-91184,24208,-29078,31495,65258,14198,85395,70506,-40908,56740,-12228,-40072,32429,93001,68445,-73927,25731,-91859,-24150,10093,-60271,-81683,-18126,51055,48189,-6468,25057,81194,-58628,74042,66158,-14452,-49851,-43667,11092,39189,-17025,-79173,13606,83172,92647,-59741,19343,-26644,-57607,82908,-20655,1637,80060,98994,39331,-31274,-61523,91225,-72953,13211,-75116,-98421,-41571,-69074,99587,39345,42151,-2460,98236,15690,-52507,-95803,-48935,-46492,-45606,-79254,-99851,52533,73486,39948,-7240,71815,-585,-96252,90990,-93815,93340,-71848,58733,-14859,-83082,-75794,-82082,-24871,-15206,91207,-56469,-93618,67131], [[-95597, -3990, 99587], [-56469, -6468, 62937], [-49851, -20655, 70506], [-41689, -40908, 82597]]),
], ids = ["happy_path_1", "happy_path_2", "happy_path_3", "edge_case_1", "edge_case_2", "error_case_1", "error_case_2", "super_long"])
def test_all(nums, expected):
    result = Solution().threeSum(nums)
    r_sets = {frozenset(r) for r in result}
    e_sets = {frozenset(e) for e in expected}
    assert not (len(r_sets)-len(e_sets) or r_sets-e_sets)
if __name__ == "__main__":
    print(Solution().test())
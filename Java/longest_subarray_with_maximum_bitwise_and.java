/*2419. Longest Subarray With Maximum Bitwise AND
Medium
You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.


Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106*/
class Solution {
    public int longestSubarray(int[] nums) {
        int max_val = 0;
        for (int i: nums) if (i>max_val) max_val = i;
        int max_count = 1;
        int index = 0;
        int sub_count = 1;
        while (index < nums.length){
            if (nums[index] != max_val){
                index++;
                sub_count = 1;
                continue;
            }
            while (index+1 < nums.length && nums[index] == nums[index+1] && nums[index] == max_val){
                sub_count++;
                index++;
            }
            index++;
            max_count = Math.max(sub_count, max_count);
        }
        return max_count;
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int[] nums = {323376,323376,323376,323376,323376,323376,323376,75940,75940}; 
        int count_4 = obj.longestSubarray(nums);
        System.out.println(count_4);
    }
}
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

    /**
     * Method to find the longest subarray with the maximum bitwise AND (i.e. 4 AND 4 is 4, but 2 AND 4 is 2)
     * @param nums (int[]): array of numbers to search
     * @return int: maximum length of continuous integers that are equal to the maximum of the input array
     */
    public int longestSubarray(int[] nums) {

        // get the maximum value in the array
        int max_val = Integer.MIN_VALUE;
        for (int i: nums) if (i>max_val) max_val = i;

        // initialize global and local maximum counts
        int max_count = 1;
        int sub_count = 0;

        // check each index for elements that equal the maximum value
        for (int i = 0; i < nums.length; i++){

            // if the max is found, increase the sub count to track continuous Integers
            if (nums[i] == max_val) sub_count++;

            // otherwise reset the sub count when the continuity breaks
            else sub_count = 0;

            // after each iteration, need to check if we found a new longest subarray that meets the conditions
            max_count = Math.max(sub_count, max_count);
        }

        // return the maximum length of the subarray with the same value that is also equal to the maximum value in the array
        return max_count;
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int[] nums = {323376,323376,323376,323376,323376,323376,323376,75940,75940}; 
        int count_4 = obj.longestSubarray(nums);
        System.out.println(count_4);
    }
}
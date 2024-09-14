
import java.util.*;

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
        int max_val = nums[0];
        HashMap<Integer, ArrayList<Integer>> indices_map = new HashMap<>();
        for (int n= 0; n < nums.length; n++){
            if (!indices_map.containsKey(nums[n])){
                indices_map.put(nums[n], new ArrayList<>(3));
            }
            indices_map.get(nums[n]).add(n);
            if (nums[n] > max_val){
                max_val = nums[n];
            }
        }
        int max_count = 0;
        int sub_count = 1;
        int prev_ind = indices_map.get(max_val).get(0);
        for (int i: indices_map.get(max_val)){
            if (i == prev_ind+1) sub_count++;
            else{
                max_count = Math.max(sub_count, max_count);
                sub_count = 1;
            }
            prev_ind = i;
        }

        return Math.max(max_count, sub_count);
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int[] nums = {1,2,3,4}; 
        int count_4 = obj.longestSubarray(nums);
        System.out.println(count_4);
    }
}
/*448. Find All Numbers Disappeared in an Array
Easy
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n

Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space. */

import java.util.*;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        boolean[] present = new boolean[n];
        for (int i = 0; i < n; i++){ present[nums[i]-1] = true; }
        List<Integer> l = new ArrayList<>();
        for(int i = 0; i < n; i++){ if (!present[i]) l.add(i+1); }
        return l;
    }
    public static void main(String[] args){
        int[] nums = {1, 3, 3, 4, 4};
        Solution obj = new Solution();
        System.out.println(obj.findDisappearedNumbers(nums));
    }
}

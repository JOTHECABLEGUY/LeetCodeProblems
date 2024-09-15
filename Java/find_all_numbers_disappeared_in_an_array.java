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

    /**
     * Method to determine which numbers are missing in the range [1, n] inclusive for an array of size n
     * @param nums (int[]): nums to look through to determine which are missing
     * @return List<Integer>: list of numbers that are missing from the input array
     */
    public List<Integer> findDisappearedNumbers(int[] nums) {

        // length of array, also stopping point of the numbers expected in the input array
        int n = nums.length;

        // array to track which elements are present in the input array
        boolean[] present = new boolean[n+1];

        // mark each element in the input array as present
        for (int i : nums){ present[i] = true; }

        // list to hold the elements that are missing
        List<Integer> l = new ArrayList<>();

        // add each missing element to the list (start at 1 and got to n, check if value in 
        //  present array is false before appending)
        for(int i = 1; i <= n; i++){ if (!present[i]) l.add(i); }

        // return the list of missing elements
        return l;
    }
    
    public static void main(String[] args){
        int[] nums = {1, 3, 3, 4, 4};
        Solution obj = new Solution();
        System.out.println(obj.findDisappearedNumbers(nums));
    }
}

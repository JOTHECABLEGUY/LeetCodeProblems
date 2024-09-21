/*55. Jump Game
Medium
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.


Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105 */

class Solution {

    /**
     * Method to determine if you can reach the last index of the array from the first index 
     *  given the maximum lengths of jumps from any index of the array
     * @param nums (int[]): array of non-negative integers representing the maximum jump length at each position.
     * @return boolean: true if the last index can be reached, false otherwise.
     */
    public boolean canJump(int[] nums) {

        // length of input array
        int n = nums.length;

        // return early if the input array has a trivial number of elements
        if (n < 2) return true;

        // keep track of maximum reachable index
        int m = 0;

        // loop until the second to last index
        for (int i = 0; i < n-1; i++){

            // if the current index is not reachable, return false
            if (i > m) return false;

            // update the max reachable index if applicable
            if (i+nums[i] > m){
                m = i + nums[i];

                // return true if the new max is sufficient to reach the last index
                if (m > n - 2) return true;
            }
        }

        // return false if the loop never reaches the final index
        return false;
    }
}

/*209. Minimum Size Subarray Sum
Medium
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
*/

class Solution {

    /**
     * Method to find the minimum length of all subarrays with a sum >= a given target
     * @param target (int): target sum that each valid subarray should sum to or above
     * @param nums (int[]): array of numbers to use to find valid subarrays
     * @return int: minimum length of a subarray such that the sum of the elements in the 
     *              subarray is greater than or equal to the given target
     */
    public int minSubArrayLen(int target, int[] nums) {

        // initialize length, sum accumulator, and left pointer
        int len = Integer.MAX_VALUE, sum = 0, l = 0;

        // start window at (0,0), increase the right bound with every iteration
        for (int r = 0; r < nums.length; r++){

            // add the rightmost value to the sum
            sum += nums[r];

            // while the sum is valid, increase the left bound (shrink window from the left)
            //  and update the sum by subtracting until the window sum is no longer reaching 
            //  the target. Update the length each time
            while (sum >= target){
                len = Math.min(len, r-l+1);
                sum -= nums[l++];
            }
        }

        // if length was never updated, it will still be the max value, meaning there is no valid
        //  subarray, so return 0, otherwise return the length
        return len == Integer.MAX_VALUE ? 0 : len;
    }

    public static void main(String[] args){
        Solution obj = new Solution();
        int target = 7;
        int[] nums = {2,3,1,2,4,3};
        System.out.println(obj.minSubArrayLen(target, nums));
    }
}
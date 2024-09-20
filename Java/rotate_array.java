/*189. Rotate Array
Medium
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space? */

class rotate_array {

    /**
     * Method to rotate a given array by a specified number of steps
     * @param nums (int[]): array of numbers to rotate
     * @param k (int): number of steps to rotate the array by
     */
    public void rotate(int[] nums, int k) {

        // if k is above the length of the array, only need to rotate by the modulo
        k %= nums.length;

        // if no rotation is needed, exit early
        if (k == 0) return;

        // array to store the correct order
        int[] correctOrder = new int[nums.length];

        // index of where next element should be inserted in the correct order
        int ins_index = 0;

        // get the last k elements of the input array, add them at the beginning of the correct order
        for (int i = nums.length - k; i < nums.length; i++) correctOrder[ins_index++] = nums[i];

        // get the first elements up to the k last elements and add them after the previous loop's stopping point
        for (int i = 0; i < nums.length-k; i++)             correctOrder[ins_index++] = nums[i];

        // copy the correct order into the input array and return
        for (int i = 0; i < nums.length; i++)               nums[i] = correctOrder[i];
    }
}

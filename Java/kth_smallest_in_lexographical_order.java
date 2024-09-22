/*440. K-th Smallest in Lexicographical Order   
Hard
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].


Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1

Constraints:

1 <= k <= n <= 109
 */

class Solution {


    public int findKthNumber(int n, int k) {

        // initialize current to be 1, decrement k
        int current = 1; k--;

        // while we haven't reached the kth element
        while (k > 0){

            // get the count of numbers lexicographically between the current and current + 1
            int count = _countSteps(n, current, current+1);

            // if the count is below or equal to k, subtract all steps from k and go on to next base
            if (count <= k) {k -= count; current++;}
            
            // reduce k by 1, multiply current by 10 to allow for the ones place to start counting
            else {k--; current *= 10;}
        }

        // once k has been depleted, current stores the kth element lexicographically
        return current;
    }

    private int _countSteps(int n, long start, long stop){

        // initialize number of steps that can be skipped
        int steps = 0;

        // while start is less than or equal to n, meaning there are still numbers that can be considered
        while (start <= n){

            // get the min of the stop and n+1 and subtract start to get the maximum number of skippable steps
            steps += Math.min(n+1, stop) - start;

            // start and stop get multiplied by 10 to consider numbers lexicographically greater
            start *= 10;
            stop *= 10;
        }

        // return the number of skippable steps between start and end
        return steps;
    }
}
/*386. Lexicographical Numbers
Medium
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 


Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]

Constraints:

1 <= n <= 5 * 104 */

import java.util.*;

class Solution {


    /**
     * Method to sort all the numbers in the range [1, n] in lexicographical order given an integer n.
     * @param n (int): limit for numbers to sort (i.e numbers that will be sorted are [1, n] inclusive)
     * @return List<Integer>: List of integers in range [1, n] sorted in lexicographical order
     */
    public List<Integer> lexicalOrder(int n) {

        // declare return list
        List<Integer> lexOrder = new ArrayList<>();

        // return early if the input number is invalid
        if (n < 1) return lexOrder;

        // for each single digit integer base, dig deeper on it to fill the list in the correct order
        for (int i = 1; i < 10; i++) 
            { dfs(lexOrder, n, i);}

        // return the assembled list
        return lexOrder;
    }

    /**
     * Recursive method to fill the array in lex order given a 
     *  current element to consider and expand upon
     * @param arr (int[]): array to add numbers to
     * @param n (int): limit of magnitude for numbers to add
     * @param current (int): current base to consider
     */
    private void dfs(List<Integer> arr, int n, int current){

        // stop digging if the current number is above the limit
        if (current > n) return;

        // add the current number to the list
        arr.add(current);

        // for each number that can be added to the current base
        for (int i = 0; i < 10; i++){

            // create a number that expands on the current base
            int new_num = current * 10 + i;

            // stop this branch if the new number is above the limit
            if (new_num > n) return;

            // expand on the new number in the list
            dfs(arr, n, new_num);
        }
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int n = 13;
        System.out.println(obj.lexicalOrder(n).toString());
    }

}
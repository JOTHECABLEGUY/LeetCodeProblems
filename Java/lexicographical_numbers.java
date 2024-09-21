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
    public List<Integer> lexicalOrder(int n) {
        List<Integer> lexOrder = new ArrayList<>();
        if (n < 1) return lexOrder;

        for (int i = 1; i < 10; i++) 
            { dfs(lexOrder, n, i);}

        return lexOrder;
        
    }

    private void dfs(List<Integer> arr, int n, int current){
        if (current > n) return;
        arr.add(current);
        for (int i = 0; i < 10; i++){
            int new_num = current * 10 + i;
            if (new_num > n) return;
            dfs(arr, n, new_num);
        }
    }

    public static void main(String[] args) {
        Solution obj = new Solution();
        int n = 13;
        System.out.println(obj.lexicalOrder(n).toString());
    }

}
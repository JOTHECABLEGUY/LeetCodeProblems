/*455. Assign Cookies
Easy
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.


Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

Constraints:

1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1 */

import java.util.*;
class Solution {
    /**
     * Method to determine the maximum number of children with minimum cookie-size requirements 
     *  that can be satisfied given an array of cookie sizes. Each cookie can go to a maximum of
     *  1 child and each child can have a maximum of 1 cookie. 
     * @param g (int[]): array of greed factors (minimum cookie size to satisfy) for each child
     * @param s (int[]): array of sizes of each cookie
     * @return int: number of children that can be satisfied with each cookie going to 0 or 1 child
     */
    public int findContentChildren(int[] g, int[] s) {

        // sort both arrays in ascending order
        Arrays.sort(g);
        Arrays.sort(s);

        // create pointers for the current position in each array, as well as a counter for the 
        //  number of satisfied children
        int g_i = 0;
        int count = 0;
        int s_i =0;
        
        // loop until no more comparisons can be made
        while (s_i < s.length && g_i < g.length){

            // check if the current size is enough to satisfy the current child's greed
            if (s[s_i] >= g[g_i]){

                // go forward in the greed array, as the current child has been satisfied
                g_i++;

                // increment the satisfied counter
                count++;
            }

            // increment the position in the size array to move to next cookie
            s_i++;
        }

        // return the number of satisfied children
        return count;
    }

    public static void main(String[] args){
        Solution obj = new Solution();
        int[] g = {10, 9, 8, 7};
        int[] s = {7, 6, 5, 4};
        System.out.println(obj.findContentChildren(g, s));
    }
}

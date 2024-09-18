/*179. Largest Number
Medium
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.


Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109 */

import java.util.*;

class Solution {

    /**
     * Method to find the largest integer result of concatenation of all elements in an input array
     * @param nums (int[]): array of numbers to concatenate
     * @return String: largest possible number created from input elements
     */
    public String largestNumber(int[] nums) {

        // convert all input numbers to Strings
        String[] str_nums = new String[nums.length];
        for (int i = 0; i < nums.length; i++){ str_nums[i] = Integer.toString(nums[i]);}

        // define a Custom Comparator to sort the input array
        Comparator<String> c = new Comparator<String>(){

            // method used to compare 2 Strings: test both ways to concatenate a pair
            //  don't swap if they are in the optimal order, sorted largest -> smallest
            @Override
            public int compare(String a, String b){
                String f = a+b; String sec = b+a; return sec.compareTo(f);
            }
        };

        // sort the array of strings using custom sorting
        Arrays.sort(str_nums, c);

        // in the case that all inputs are 0, return as soon as possible
        if (str_nums[0].charAt(0) == '0') return "0";

        // concatenate the Strings using a StringBuilder and return it after converting to a base String
        StringBuilder final_num = new StringBuilder();
        for (String n:str_nums) final_num.append(n);
        return final_num.toString();
    }
}
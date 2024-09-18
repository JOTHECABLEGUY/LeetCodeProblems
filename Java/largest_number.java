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
    public String largestNumber(int[] nums) {
        String[] str_nums = new String[nums.length];
        for (int i = 0; i < nums.length; i++){ str_nums[i] = Integer.toString(nums[i]);}
        Comparator<String> c = new Comparator<>(){
            @Override
            public int compare(String a, String b){
                String f = a+b; String sec = b+a; return sec.compareTo(f);
            }
        };
        Arrays.sort(str_nums, c);
        if (str_nums[0].charAt(0) == '0') return "0";
        StringBuilder final_num = new StringBuilder();
        for (String n:str_nums) final_num.append(n);
        return final_num.toString();
    }
    
}
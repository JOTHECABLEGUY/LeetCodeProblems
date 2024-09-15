/*
1371. Find the Longest Substring Containing Vowels in Even Counts
Medium
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.


Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters.*/

import java.util.*;

class Solution {

    /**
     * Method to find the longest substring in a string such that the counts of all vowels
     *  in the substring are even. Consonant counts do not matter
     * @param s (String): String to search for subarrays
     * @return int: length of longest substring such that the counts of all vowels are even
     */
    public int findTheLongestSubstring(String s) {

        // mask to keep track of vowel counts
        int mask = 0;

        // map to track indices of the first occurrence of vowel parities (states)
        HashMap<Integer, Integer> memo = new HashMap<>();

        // add a first pair to the map for the first position
        memo.put(0, -1);

        // track the largest relevant substring
        int result = 0;

        // check each char in the input String
        for (int i = 0; i < s.length(); i++){

            // if the char is a vowel, xor the mask with 1, shifted a certain amount of places depending on 
            //  the vowel's relative position in the English alphabet, do nothing if it's a consonant
            switch (s.charAt(i)) {
                case 'a': mask = mask ^ 1; break;
                case 'e': mask = mask ^ 1 << 1; break;
                case 'i': mask = mask ^ 1 << 2; break;
                case 'o': mask = mask ^ 1 << 3; break;
                case 'u': mask = mask ^ 1 << 4; break;
                default: break;
            }

            // if the mask was seen before, we know that everything between this position
            //  and the first occurrence of the mask is part of a valid substring. Update 
            //  the result if the current length of the substring is larger than the current max
            if (memo.containsKey(mask)) result = Math.max(result, i - memo.get(mask));

            // otherwise, add the index to the map as the first occurrence of the mask
            else memo.put(mask, i);
        }

        // return the result: the longest substring matching the conditions
        return result;
    }
    
    public static void main(String[] args){
        String s1 = "eleetminicoworoep";
        String s2 = "leetcodeisgreat";
        String s3 = "bcbcbc";
        Solution obj = new Solution();
        System.out.println("Found " + obj.findTheLongestSubstring(s1) + " Expected " + 13);
        System.out.println("Found " + obj.findTheLongestSubstring(s2) + " Expected " + 5);
        System.out.println("Found " + obj.findTheLongestSubstring(s3) + " Expected " + 6);
    }
}

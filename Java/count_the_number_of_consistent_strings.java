/* 1684. Count the Number of Consistent Strings
Easy
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters. */

class Solution {

    /* Method to count the number of string from the input list of strings that 
        only contain the letters found in a given input string
    @param allowed (String): string containing valid characters
    @param words (String[]): array of words that to be checked against the allowed string
    @returns int: Count of words that only contain the letters found in the allowed input String.
        Valid words do not to contain EVERY allowed letter, but they cannot contain any others.
    */
    public int countConsistentStrings(String allowed, String[] words) {

        // for each lowercase letter, store whether it is allowed or not
        boolean[] present = new boolean[26];

        // for each char in the allowed, set its value to true in the boolean array
        for (char ch : allowed.toCharArray()){
            present[ch-'a'] = true;
        }

        // counter for number of valid strings
        int count = 0;

        // check each word
        for (String word:words){

            // flag for whether the current string is allowed
            boolean flag = true;

            // check the letters in the current word. If a char isnt present in the allowed string, set the flag to false and break
            for (int c = 0; c < word.length(); c++){
                if (!present[word.charAt(c)-'a']){
                    flag = false;
                    break;
                }
            }

            // after the loop finishes, increment the counter if the loop did not end early (all chars in the word were in teh allowed string)
            if (flag==true) count++;
        }

        // return the count of valid words
        return count;
    }

    // main method to run program
    public static void main(String args[]){
        Solution result = new Solution();
        String input_allowed = "ab";
        String[] words = {"ab", "ad", "ababdaaba", "a", "abbbbbbbbbbbbbbbbbbba"};
        int res = result.countConsistentStrings(input_allowed, words);
        System.out.println("result = " + res);
    }
    
}

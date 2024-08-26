"""3. Longest Substring Without Repeating Characters
Medium
Given a string s, find the length of the longest 
substring
without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces."""

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_dist = 0,0
        index_map = defaultdict(lambda: -1)
        for right in range(len(s)):
            char = s[right]
            prev_index = index_map[char]
            if prev_index != -1:
                left = max(left, prev_index + 1)
            index_map[char] = right
            max_dist = max(max_dist, right-left+1)
        return max_dist
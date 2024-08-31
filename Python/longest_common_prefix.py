"""14. Longest Common Prefix
Easy
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""
import pytest
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            Finds the longest common prefix among a list of strings.

            This function takes a list of strings and returns the longest common prefix shared 
            by all the strings in the list. If there is no common prefix, it returns an empty string.

            Args:
                strs (List[str]): A list of strings to evaluate for the longest common prefix.

            Returns:
                str: The longest common prefix found in the list of strings, or an empty string 
                if no common prefix exists.
        """
        # if smallest string is empty, return nothing
        if not (min_str_len := min(len(s) for s in strs)):
            return ""
        # for each index in the smallest string, build a set with each character at the same position
        #   if any characters are different, the set will have a length greater than 1, so decrement i 
        #   and break the loop, otherwise continue
        for i in range(min_str_len):
            if len({s[i] for s in strs})-1:
                i-=1
                break
        
        # once the loop breaks, we know that the longest common prefix is from indices 0 to i+1 (when the loop
        #   ends, either i was decremented or i = the last index of the string), so i needs to be 1 more in 
        #   order for the slicing to capture all the characters (slicing stops 1 before the supplied index).
        return strs[0][:i+1]
    def test(self):
        return self.longestCommonPrefix(["dog", "dog", "dog"])
@pytest.mark.parametrize(
        "strings, expected", 
    [
        (["dog", "dogbone", "debt"], "d"),
    ], 
        ids = ["single char in common"]
)
def test_all(strings, expected):
    result = Solution().longestCommonPrefix(strings)
    assert result == expected
if __name__ == "__main__":
    print(Solution().test())
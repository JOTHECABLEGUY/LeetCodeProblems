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
        min_str_len = min(len(s) for s in strs)
        c = [""]*min_str_len
        for i in range(min_str_len):
            char = strs[0][i]
            chars = [s[i] for s in strs]
            if any(char != c for c in chars):
                break
            c[i] = char
        return "".join(c)
    def test(self):
        return self.longestCommonPrefix(["dog", "dogbone", "debt"])
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
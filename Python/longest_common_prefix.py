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
        if not (strs and (min_str_len := min(len(s) for s in strs))):
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
        # Happy path tests
        (["flower", "flow", "flight"], "fl"),  # common prefix "fl"
        (["dog", "racecar", "car"], ""),       # no common prefix
        (["interspecies", "interstellar", "interstate"], "inters"),  # common prefix "inters"
        (["throne", "throne"], "throne"),      # identical strings

        # Edge cases
        ([""], ""),                            # single empty string
        (["a"], "a"),                          # single character string
        (["", "b"], ""),                       # one empty string
        (["prefix", "prefixes", "prefixing"], "prefix"),  # common prefix is the entire first string
        (["pre", "prefix", "prefixing"], "pre"),  # common prefix "pre"
        (["a", "ab", "abc"], "a"),             # common prefix "a"

        # Error cases
        ([], ""),                              # empty list
], ids=[
    "common_prefix_fl",
    "no_common_prefix",
    "common_prefix_inters",
    "identical_strings",
    "single_empty_string",
    "single_character_string",
    "one_empty_string",
    "common_prefix_entire_first_string",
    "common_prefix_pre",
    "common_prefix_a",
    "empty_list"
])
def test_all(strings, expected):
    result = Solution().longestCommonPrefix(strings)
    assert result == expected
if __name__ == "__main__":
    print(Solution().test())
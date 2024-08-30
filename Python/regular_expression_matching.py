"""10. Regular Expression Matching
Hard
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).


Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match."""

import re, pytest
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.match(rf"^{p}$", s))
    def test(self):
        return self.isMatch(r"a", r"")
if __name__ == "__main__":
    print(Solution().test())
@pytest.mark.parametrize("s, p, expected", [
    # happy path tests
    ("abc", "abc", True),  # exact match
    ("abc", "a.c", True),  # single character wildcard
    ("abbbbc", "ab*c", True),  # zero or more of preceding element
    ("aab", "c*a*b", True),  # complex pattern with zero or more and exact match

    # edge cases
    ("", "", True),  # both strings empty
    ("", "a*", True),  # empty string with zero or more pattern
    ("a", "", False),  # non-empty string with empty pattern
    ("", ".", False),  # empty string with single character wildcard

    # error cases
    ("abc", "abcd", False),  # pattern longer than string
    ("abc", "ab*d", False),  # pattern does not match string
    ("abc", "a.*d", False),  # pattern almost matches but fails
], ids=[
    "exact_match",
    "single_char_wildcard",
    "zero_or_more_preceding",
    "complex_pattern",
    "both_empty",
    "empty_string_zero_or_more",
    "non_empty_string_empty_pattern",
    "empty_string_single_char_wildcard",
    "pattern_longer_than_string",
    "pattern_does_not_match",
    "pattern_almost_matches"
])
def test_isMatch(s, p, expected):

    # Act
    result = Solution().isMatch(s, p)

    # Assert
    assert result == expected
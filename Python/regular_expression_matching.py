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


from itertools import product
import re, pytest
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return bool(re.match(rf"^{p}$", s))
    def isMatch_2(self, s: str, p: str) -> bool:
        """
            Determines if a string matches a given pattern using regular expression rules.

            This function implements a dynamic programming approach to check if the input string 
            matches the specified pattern, which may include wildcard characters such as '.' and '*'. 
            The function returns True if the string matches the pattern, and False otherwise.

            Args:
                s (str): The input string to be matched against the pattern.
                p (str): The pattern string that may contain wildcard characters.

            Returns:
                bool: True if the string matches the pattern, False otherwise.
        """
        
        # if no pattern was provided (empty string), return True if the string to check is also empty, False if otherwise
        if not p:
            return not s
        
        # set up table to keep track of previously calculated steps
        s_len, p_len = len(s), len(p)
        cache = [[False] * (p_len+1) for _ in range(s_len + 1)]
        cache[0][0] = True
        
        # pre fill cells that will be used later due to the 0 or more nature of the asterisk
        #   more specifically, the loops after this will end up propagating the value down the table. 
        for i in range(1, p_len+1):
            if p[i-1] == '*':
                cache[0][i] = cache[0][i-2]
            
        # loop through the string and pattern together (start at 1 since the 0 rows/columns were used for pre filled values)
        for s_pointer, p_pointer in product(range(1, s_len+1), range(1, p_len+1)):
            
            # first check if there is a straight match, no more fancy logic is required if there is no asterisk,
            #   just fill in false or true depending on if the string matches the pattern at the relevant positions
            if p[p_pointer-1] in {s[s_pointer-1], '.'}:
                cache[s_pointer][p_pointer] = cache[s_pointer-1][p_pointer-1]
            
            # if the first check failed, check for an asterisk '*' char in the pattern
            elif p[p_pointer-1] == '*':
                
                # the possible checks for this branch are listed below:
                #   check 1: if the pattern matched the string up until 2 chars ago (skipping over the char* altogether), then it could be true. Check the AND condition
                #   check 2: if the string matched the pattern up until the last char (the string has one or more of the repeated char before), 
                #               then it could be true. Check the AND condition
                #   check 3: check that the char that came before the asterisk pair was either a wildcard or matched the last char from the string
                cache[s_pointer][p_pointer] =(cache[s_pointer][p_pointer-2]                 # check 1
                                            or cache[s_pointer-1][p_pointer]                # check 2
                                            and p[p_pointer-2] in {s[s_pointer-1], '.'})    # check 3
        
        return cache[s_len][p_len]
    def test(self):
        return self.isMatch_2(r"ab", r"a*b")
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
    result = Solution().isMatch_2(s, p)

    # Assert
    assert result == expected
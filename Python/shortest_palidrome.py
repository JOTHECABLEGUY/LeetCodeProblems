"""214. Shortest Palindrome
Hard
You are given a string s. You can convert s to a 
palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.


Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only."""

import pytest

class Solution:
    
    def test(self):
        return self.shortestPalindrome("abcd"), self.shortestPalindrome("aacecaaa")
    
    def shortestPalindrome(self, s: str) -> str:
        """
            Find the shortest palindrome by adding characters to the beginning of the given string.

            This function takes a string and determines the minimum characters needed to be added to its 
            start to make it a palindrome. It efficiently computes the result using a combination of string 
            reversal and the Knuth-Morris-Pratt (KMP) algorithm to identify the longest palindromic prefix.

            Args:
                s (str): The input string to be transformed into a palindrome.

            Returns:
                str: The shortest palindrome that can be formed by adding characters to the beginning of the input string.
        """
        
        # return early if no need to add chars
        if len(s) < 2: return s
        
        # take the reverse of the string and append it to the original string with a # separator
        r = s[::-1]
        c = f"{s}#{r}"
        
        # allocate a list of 0s to track how many characters the reverse and the forward have in common
        kmp = [0] * len(c)
        
        # index within the combined string
        j = 0
        
        # loop through the combined string, filling in the list at index i
        for i in range(1, len(c)):
            
            # get the prefix match of the string before i
            j = kmp[i - 1]
            
            # go back in the kmp array while the chars at i and j are different
            while j > 0 and c[i] != c[j]:
                j = kmp[j - 1]
            
            # when the loop breaks, if the second condition is what the loop exited on,
            #   increase j as there is one more element in common
            if c[i] == c[j]:
                j += 1
                
            # update the number of common chars for string of length i 
            kmp[i] = j
            
        # add the chars outside of the shared sequence to the beginning of the original string
        return f"{r[:-kmp[-1]]}{s}"

@pytest.mark.parametrize("input_str, expected_output", [
    # happy path tests
    ("aacecaaa", "aaacecaaa"),  # simple case
    ("abcd", "dcbabcd"),        # no palindrome prefix
    ("racecar", "racecar"),     # already a palindrome

    # edge cases
    ("", ""),                   # empty string
    ("a", "a"),                 # single character
    ("aa", "aa"),               # two identical characters
    ("ab", "bab"),              # two different characters

    # error cases
    ("a" * 1000, "a" * 1000),   # long string of identical characters
    ("a" * 999 + "b", "b" + "a" * 999 + "b"),  # long string with one different character at the end
], ids=[
    "simple_case",
    "no_palindrome_prefix",
    "already_palindrome",
    "empty_string",
    "single_character",
    "two_identical_characters",
    "two_different_characters",
    "long_identical_characters",
    "long_one_different_character"
])
def test_shortestPalindrome(input_str, expected_output):

    # Act
    result = Solution().shortestPalindrome(input_str)

    # Assert
    assert result == expected_output

if __name__ == "__main__":
    print(Solution().test())
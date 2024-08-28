"""5. Longest Palindromic Substring
Medium
Given a string s, return the longest 
palindromic substring in s.


Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters."""
import pytest
class Solution:
    def test(self):
        return self.longestPalindrome("babad")
    def is_palidromic(self, s:str) -> bool:
        s_length = len(s)
        middle_index = s_length//2
        first_half = s[:middle_index]
        second_half = s[middle_index+1:] if s_length % 2 else s[middle_index:]
        return first_half == second_half[::-1]

    # complexity: O(n^3)
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        max_len_seq = ""
        if not s:
            return max_len_seq
        length_of_input_string = len(s)
        for i in range(length_of_input_string):
            for j in range(length_of_input_string, i, -1):
                seq = s[i:j]
                if (seq_len := len(seq)) <= max_len:
                    continue
                if self.is_palidromic(seq) and seq_len > max_len:
                    max_len_seq = seq
                    max_len = seq_len
        return max_len_seq
    
    # complexity: O(n^2)
    def longestPalindrome_2(self, s:str) -> str:
        max_len:int = 0
        max_sub:str = ""
        max_start = 0
        if len(s) == 1: 
            return s

        if len(s) == 2:
            return s[0] if s != s[::-1] else s
        # even length palidromes
        for i in range(len(s)-1):
            left = i
            right = i+1
            while(right < len(s) and left >= 0 and s[left] == s[right]):
                right += 1
                left -= 1
            new_len = right-left+1
            if new_len > max_len:
                max_len = new_len
                max_start = left

        # odd length palindromes
        for i in range(len(s)-2):
            left = i
            right = i+2
            while(right < len(s) and left >= 0 and s[left] == s[right]):
                right += 1
                left -= 1
            new_len = right-left+1
            if new_len > max_len:
                max_len = new_len
                max_start = left
        return s[max_start+1:max_start+max_len]
            
                    


@pytest.mark.parametrize("input_str, expected_output", [
    # Happy path tests
    ("babad", "bab"),  # "bab" and "aba" are both valid, but "bab" is expected
    ("cbbd", "bb"),    # "bb" is the longest palindrome
    ("a", "a"),        # Single character string
    ("ac", "a"),       # No palindrome longer than 1 character

    # Edge cases
    ("", ""),          # Empty string
    ("aaaa", "aaaa"),  # All characters are the same
    ("abcba", "abcba"),# Entire string is a palindrome
    ("abcdefghijklmnopqrstuvwxyzzabcdefghijklmnopqrstuvwxyz", "zz"),

    # Error cases
    ("abacdfgdcaba", "aba"), # Multiple palindromes, "aba" is the longest
], ids=[
    "happy_path_1",
    "happy_path_2",
    "happy_path_3",
    "happy_path_4",
    "edge_case_empty_string",
    "edge_case_all_same_characters",
    "edge_case_entire_string_palindrome",
    "edge_case_longer_string",
    "error_case_multiple_palindromes"
])
def test_longestPalindrome(input_str, expected_output):
    # Arrange
    solution = Solution()

    # Act
    result = solution.longestPalindrome_2(input_str)

    # Assert
    assert result == expected_output
if __name__ == "__main__":
    print(Solution().test())
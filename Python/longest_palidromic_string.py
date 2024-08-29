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
    def is_palindrome(self, s:str) -> bool:
        """
            Check if a given string is a palindrome.

            This function compares the first half of the string to the reversed second half to determine if the string reads the same forwards and backwards.

            Args:
                s (str): The input string to check for palindromic properties.

            Returns:
                bool: True if the input string is a palindrome, False otherwise.

            Raises:
                None
        """
        s_length = len(s)
        middle_index = s_length//2
        first_half = s[:middle_index]
        second_half = s[middle_index+1:] if s_length % 2 else s[middle_index:]
        return first_half == second_half[::-1]

    # complexity: O(n^3), brute force approach
    def longestPalindrome(self, s: str) -> str:
        """
            Find the longest palindromic substring in a given string.

            This function iterates through all possible substrings of the input string, checking each one for palindromic properties, and returns the longest palindromic substring found.

            Args:
                s (str): The input string to search for palindromic substrings.

            Returns:
                str: The longest palindromic substring found in the input string. If no palindromic substring exists, an empty string is returned.

            Raises:
                None

            Examples:
                longestPalindrome_2(self, "babad")  # Returns "bab" or "aba"
                longestPalindrome_2(self, "cbbd")   # Returns "bb"
        """
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
                if self.is_palindrome(seq) and seq_len > max_len:
                    max_len_seq = seq
                    max_len = seq_len
        return max_len_seq
    
    # helper function to expand around a given center; O(n). 
    #   If left == right, looking for odd length substrings,
    #   If left != right, looking for even length substrings
    def expand(self, left:int, right:int, s:str)-> int:
        """
            Expand around the given indices to find the length of the palindromic substring.

            This function checks characters in the string from the specified left and right indices, expanding outwards as long as the characters match, and returns the length of the palindrome found.

            Args:
                left (int): The starting index on the left side for expansion.
                right (int): The starting index on the right side for expansion.
                s (str): The input string to check for palindromic substrings.

            Returns:
                int: The length of the palindromic substring found.

            Raises:
                None
        """
        s_len = len(s)
        while left >= 0 and right < s_len and s[left] == s[right]:
            left -= 1
            right += 1
            
        # the condition for ending the while loop is the pointers exceed the bounds of the string 
        #   or left does not equal right, meaning the pointers are currently not correct. 
        #   We account for this by subtracting 2 from the original distance (orig dist = right-left+1)
        return right-left-1
    # complexity: O(n^2), expand around centers approach
    def longestPalindrome_2(self, s:str) -> str:
        """
            Find the longest palindromic substring in a given string.

            This function checks for palindromic substrings by expanding around potential centers and returns the longest one found.

            Args:
                s (str): The input string to search for palindromic substrings.

            Returns:
                str: The longest palindromic substring found in the input string.

            Raises:
                None

            Examples:
                longestPalindrome_2(self, "babad")  # Returns "bab" or "aba"
                longestPalindrome_2(self, "cbbd")   # Returns "bb"
        """
        max_dist:int = 0
        max_start = 0
        s_len = len(s)
        
        # quit early if a palindromic input string is supplied or the length is 2
        if s == s[::-1]:
            return s
        if s_len == 2:
            return s[0]
        
        # the last char in the string cannot be the center of the longest palindrome 
        #   (the second to last would capture the last char in its own palindrome)
        for center in range(s_len-1):
            odd_dist = self.expand(center, center, s)
            even_dist = self.expand(center, center+1, s)
            
            # use radius to find the starting index of substring (due to mirror nature of palindromes)
            if odd_dist > max_dist:
                max_start = center - (odd_dist//2)     # center - radius
                max_dist = odd_dist
            if even_dist > max_dist:
                max_start = center - (even_dist//2 - 1) # center - radius
                max_dist = even_dist
            
        return s[max_start: max_start + max_dist]

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
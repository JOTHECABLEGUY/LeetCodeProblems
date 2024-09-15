"""1371. Find the Longest Substring Containing Vowels in Even Counts
Medium
Given the string s, return the size of the longest substring containing each vowel an even number of times. That is, 'a', 'e', 'i', 'o', and 'u' must appear an even number of times.


Example 1:

Input: s = "eleetminicoworoep"
Output: 13
Explanation: The longest substring is "leetminicowor" which contains two each of the vowels: e, i and o and zero of the vowels: a and u.
Example 2:

Input: s = "leetcodeisgreat"
Output: 5
Explanation: The longest substring is "leetc" which contains two e's.
Example 3:

Input: s = "bcbcbc"
Output: 6
Explanation: In this case, the given string "bcbcbc" is the longest because all vowels: a, e, i, o and u appear zero times.

Constraints:

1 <= s.length <= 5 x 10^5
s contains only lowercase English letters."""

import pytest

class Solution:
    
    def test(self):
        return self.findTheLongestSubstring("eleetminicoworoep")
    
    def findTheLongestSubstring(self, s: str) -> int:
        """
            Determine the length of the longest substring with an even count of vowels.

            This function analyzes a given string and calculates the length of the longest
            contiguous substring where each vowel appears an even number of times. If no such
            substring exists, the function returns 0.

            Args:
                s (str): The input string to evaluate.

            Returns:
                int: The length of the longest substring with even counts of vowels.
        """
        
        # maximum length of the required substring
        max_len = 0
        
        # bit mask to keep track of parity (even/odd counts of vowels)
        mask = 0 # 0x00000
        
        # dictionary to track the last occurrence of the current state of the mask
        prev_states = {mask: -1}
        
        # set to test if the current character is a vowel
        vowels = {'a','e','i','o','u'}
        
        # for each position in the string
        for i in range(len(s)):
            
            # if a vowel is found, toggle the appropriate place in the mask using the 
            #   previous mask state and the ascii codes for the letter. i.e. if i have a letter A
            #   and the mask is currently 0, then ord(char) -ord('a') + 1 = ord('a') - ord('a') + 1 
            #   = 1, so mask ^ 1 = 0 ^ 1 = 1, thus the first bit from the right is toggled to 1 since 
            #   a single A has been seen. Further, if we encounter another A, the same expression
            #   will evaluate to 1^1, resulting in the "A bit" being set to 0, meaning the current
            #   substring has an even amount of As. If a U was then processed, the same expression
            #   would result in the first bit from the left being toggled
            if s[i] in vowels:
                mask ^= (ord(s[i]) - ord('a')+1)
                
            # once the mask has been updated, check if the state has been seen before, meaning that 
            #   the current numbers of vowels have the same parity as an iteration before. If this is the
            #   case, the length of the substring that matches this state is the first occurrence of this state
            #   taken from the current index. Update the max if this length is larger
            if mask in prev_states:
                max_len = max(max_len, i - prev_states[mask])
            
            # otherwise, this is the first time seeing this state, so we can mark this index in the state
            #   dictionary to use in a future iteration
            else:
                prev_states[mask] = i

        # return the maximum length of the substring with the conditions met
        return max_len

@pytest.mark.parametrize(
    "s, expected",
    [
        # Happy path tests
        ("eleetminicoworoep", 13),  # All vowels in even counts
        ("leetcodeisgreat", 5),     # Substring "leetc" has even counts
        ("bcbcbc", 6),              # No vowels, entire string is valid

        # Edge cases
        ("", 0),                    # Empty string
        ("a", 0),                   # Single vowel
        ("b", 1),                   # Single consonant
        ("aeiou", 0),               # All vowels, no even counts
        ("aeiouaeiou", 10),         # All vowels in even counts
        ("xyz", 3),                 # No vowels, entire string is valid
        ("aeiobcdeiou", 9),         # Mixed vowels and consonants
    ],
    ids=[
        "all_vowels_even_counts",
        "substring_with_even_counts",
        "no_vowels",
        "empty_string",
        "single_vowel",
        "single_consonant",
        "all_vowels_no_even_counts",
        "all_vowels_even_counts_long",
        "no_vowels_entire_string",
        "mixed_vowels_and_consonants",
    ]
)
def test_findTheLongestSubstring(s, expected):

    # Act
    result = Solution().findTheLongestSubstring(s)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
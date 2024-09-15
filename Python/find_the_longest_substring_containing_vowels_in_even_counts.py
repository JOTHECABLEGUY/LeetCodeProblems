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
        
        max_len = 0
        counter = [0,0,0,0,0]
        d = {tuple(counter): -1}
        vowels = ['a','e','i','o','u']
        for index, l in enumerate(s):
            if l in vowels:
                i = vowels.index(l)
                counter[i] = 1 - counter[i] # toggle
            tup = tuple(counter)
            if tup in d:
                max_len = max(max_len, index - d[tup])
            else:
                d[tup] = index

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
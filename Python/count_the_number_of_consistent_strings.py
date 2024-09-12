"""1684. Count the Number of Consistent Strings
Easy
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters."""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.countConsistentStrings("ab", ["aba", "abd", "abbbbabababaabababaab", "abababababaababadbabababaab"])
    
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        if not isinstance(allowed, str):
            return 0
        s = set(allowed)
        return len([w for w in words if isinstance(w, str) and not set(w)-s])

@pytest.mark.parametrize(
    "allowed, words, expected",
    [
        # Happy path tests
        ("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"], 7),
        ("abc", ["a", "b", "c", "d", "ab", "ac", "bc", "abc"], 7),
        
        # Edge cases
        ("", ["a", "b", "c"], 0),
        ("abc", [], 0),
        ("a", ["a", "aa", "aaa"], 3),
        
        # Error cases
        ("abc", ["a", "b", "c", 123], 3),
        (123, ["a", "b", "c"], 0),
    ],
    ids=["all_words_allowed", "one_word_not_allowed", "no_allowed_characters", "no_words", "single_allowed_character", "non_string_word", "non_string_allowed"]
)
def test_countConsistentStrings(allowed, words, expected):

    # Act
    result = Solution().countConsistentStrings(allowed, words)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
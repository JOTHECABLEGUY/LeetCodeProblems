"""884. Uncommon Words from Two Sentences
Easy
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.


Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]


Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space."""

import pytest
from collections import defaultdict
from typing import List

class Solution:
    
    def build_counter(self, s):
        
        res = defaultdict(int)
        for t in s.split(' '):
            res[t] += 1
        return res
    
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_counter = self.build_counter(s1)
        s2_counter = self.build_counter(s2)
        
        if not s1:
            return [k for k, c in s2_counter.items() if c < 2] if s2 else []
        if not s2:
            return [k for k, c in s1_counter.items() if c < 2] if s1 else []
        
        return [k for k in s1_counter.keys() ^ s2_counter.keys() if s1_counter[k] < 2 and s2_counter[k] < 2]

@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        # Happy path tests
        ("this apple is sweet", "this apple is sour", ["sweet", "sour"]),
        ("apple apple", "banana", ["banana"]),
        ("", "banana", ["banana"]),
        ("apple", "", ["apple"]),
        
        # Edge cases
        ("", "", []),
        ("a a a", "b b b", []),
        ("a b c", "a b c", []),
        
        # Error cases
        ("a b c", "a b c d", ["d"]),
        ("a b c d", "a b c", ["d"]),
    ],
    ids=[
        "common words with different counts",
        "one sentence with repeated words",
        "empty first sentence",
        "empty second sentence",
        "both sentences empty",
        "repeated words in both sentences",
        "identical sentences",
        "one extra word in second sentence",
        "one extra word in first sentence",
    ]
)
def test_uncommonFromSentences(s1, s2, expected):
    # Arrange
    solution = Solution()

    # Act
    result = solution.uncommonFromSentences(s1, s2)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().uncommonFromSentences("s z z z s", "s ejt z"))
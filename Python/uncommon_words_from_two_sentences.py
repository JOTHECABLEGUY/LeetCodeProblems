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
from collections import defaultdict, Counter
from typing import List

class Solution:
    
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        """
            Find the uncommon words from two sentences.

            This function takes two sentences as input and returns a list of words that are present
            in one sentence but not in the other. Words that appear more than once in either sentence
            are excluded from the result.

            Args:
                s1 (str): The first sentence.
                s2 (str): The second sentence.

            Returns:
                List[str]: A list of uncommon words found in either sentence.
        """
        
        # build counters for the tokens in the sentences
        s1_counter = Counter(s1.split(' '))
        s2_counter = Counter(s2.split(' '))
        
        # filter down to only words that occur at most once in one or both sentences
        s1_tokens = {w for w in s1_counter if s1_counter[w] < 2 and s2_counter[w] < 2}
        s2_tokens = {w for w in s2_counter if s1_counter[w] < 2 and s2_counter[w] < 2}
        
        # if one of the sentences is empty, just return the tokens that occur in the other 
        #   sentence if it isn't empty, otherwise return an empty list
        if not s1:
            return list(s2_tokens) if s2 else []
        if not s2:
            return list(s1_tokens) if s1 else []
        
        # return the list of tokens that only occur in one sentence (they are guaranteed to be uncommon at this point)
        return list(s1_tokens ^ s2_tokens)

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
    assert set(result) == set(expected)

if __name__ == "__main__":
    print(Solution().uncommonFromSentences("s z z z s", "s ejt z"))
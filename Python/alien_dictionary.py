"""269. Alien Dictionary
Hard
There is a new alien language that uses the English alphabet. However, the order among
the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings
in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically
increasing order by the new language's rules. If there is no solution, return ""

If there are
multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they
differ, the letter in s comes before the letter in t in the alien language. If the first
min(s.length, t.length) letters are the same, then s is smaller if and only if 
s.length < t.length.

Example 1:
words = ["wrt","wrf","er", "ett", "rftt"]
Input: words
Output: "wertf"
"""
import pytest
from typing import List
class Solution:
    
    def test(self):
        return self.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
    
    def alienOrder(self, words:List[str]):
        """
            Determines the order of characters in an alien language based on a list of words.

            This function constructs a directed graph from the given words to represent the relationships between characters. 
            It then performs a depth-first search to derive the correct order of characters, returning an empty string if a cycle is detected.

            Args:
                words (List[str]): A list of words representing the alien language.

            Returns:
                str: A string representing the characters in the correct order, or an empty string if the order cannot be determined.
        """
        
        # build base for graph: each character given will have an adjacency set
        adj_map = {c:set() for c in set("".join(words))}
        
        # process each pair of words
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            
            # if the first word is longer than the second word, and the second word is wholly contained in the
            #   prefix of the first word, return an empty string as the given alien dictionary is not valid 
            if w1.startswith(w2) and len(w1) > len(w2):
                return ""
            
            # get minimum length of the 2 words
            min_len = min(len(w2), len(w1))
            
            # loop through the characters of both strings
            for j in range(min_len):
                
                # if the characters differ at the current position, we know that the character in the second word
                #   must come before the character from the first word, so add a directed edge into the adjacency
                #   map then break the loop since only the first differing characters are discriminating
                if w1[j] != w2[j]:
                    adj_map[w1[j]].add(w2[j])
                    break
        
        # make a dictionary to store character -> bool mappings: not in the map means it hasn't been seen yet,
        #   False means that it has been seen but it is not currently in the path, True means that it has been seen
        #   and it is in the current path
        visited = {}
        
        # result list for post-order traversal
        res = []
        
        # depth first search recursive helper function
        def dfs(letter):
            
            # if the letter has already been seen previously, return the value stored
            if letter in visited:
                return visited[letter]
            
            # set the value for the current character in the dictionary to True, as we have seen it 
            #   and it is in the current path of traversal
            visited[letter] = True
            
            # for each letter that must come after the current letter, check that the recursive DFS is 
            #   True (meaning that there is a cycle). If any character is in a cycle, return True
            if any(dfs(postreq) for postreq in adj_map[letter]):
                return True
            
            # set the current characters boolean value to False (backtrack)
            visited[letter] = False
            
            # add the letter to the end of the result list
            res.append(letter)
            
            # return False, as that is the value for the current character
            return False
        
        # if any DFS is true for the characters in the language, return an empty string
        #   meaning that a valid ordering of characters is not possible. Otherwise, join the
        #   letters stored in the result list (but we need to reverse the list since post-order
        #   traversal was used).
        return "" if any(dfs(c) for c in adj_map) else "".join(res[::-1])

@pytest.mark.parametrize("words, expected", [
    # Happy path tests
    (["wrt", "wrf", "er", "ett", "rftt"], "wertf"),
    (["z", "x"], "zx"),
    (["z", "x", "z"], ""),
    # Edge cases
    (["abc", "ab"], ""),
    (["a", "b", "c"], "abc"),
    (["a", "a"], "a"),
    ([], ""),
    (["a"], "a"),
    (["ab", "adc"], {"abcd", "bcad", "acbd", "cabd", "bacd", "cbad", "abdc", "cbda", "bdca", "bdac"}),
], ids=[
    "happy_path_1",
    "happy_path_2",
    "happy_path_3",
    "edge_case_1",
    "edge_case_2",
    "edge_case_3",
    "edge_case_4",
    "edge_case_5",
    "edge_case_6",
])
def test_alienOrder(words, expected):

    # Act
    result = Solution().alienOrder(words)

    # Assert
    assert result in expected

if __name__ == "__main__":
    print(Solution().test())
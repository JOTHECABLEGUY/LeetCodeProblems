"""22. Generate Parentheses
Medium
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8"""

import pytest
from typing import List
class Solution:
    def test(self):
        return self.generateParenthesis(3)
    
    def gen_next_parentheses(self, open_count:int, closed_count:int, curr:str, n:int, out: List[str]):
        """
            Generates the next valid parentheses combination.

            This recursive function builds valid combinations of parentheses by tracking 
            the number of open and closed parentheses used. It appends valid combinations 
            to the output list when the current combination reaches the expected length.

            Args:
                open_count (int): The current count of open parentheses.
                closed_count (int): The current count of closed parentheses.
                curr (str): The current string representing the combination of parentheses.
                n (int): The total number of pairs of parentheses to generate.
                out (List[str]): The list to store the valid combinations generated.

            Returns:
                None: This function modifies the output list in place and does not return a value.
        """
        # base case: exit when number of closed plus number of open is one less than expected length (3 open, 2 closed)
        #   this condition is enforced by the building process below (rather than additional recursive calls,
        #   just add ')' to the end of each appended string)
        if open_count + closed_count == n*2 - 1:
            out.append(curr)
            return
        
        # can only add ( if number of open parentheses is below number of pairs requested.
        # increment open count and run with an open parenthesis added
        if open_count < n:
            self.gen_next_parentheses(open_count+1, closed_count, f'{curr}(', n, out)

        # can only add ) if number of closed parentheses is below number of open parentheses.
        # increment closed count and run with a closed parenthesis added
        if closed_count < open_count:
            self.gen_next_parentheses(open_count, closed_count+1, f'{curr})', n, out)
            
    def generateParenthesis(self, n: int) -> List[str]:
        """
            Generates all combinations of valid parentheses.

            This function generates all combinations of well-formed parentheses for a given 
            number of pairs, n. It utilizes a recursive helper function to build valid combinations 
            and returns a list of these combinations.

            Args:
                n (int): The number of pairs of parentheses to generate.

            Returns:
                List[str]: A list of strings representing all combinations of valid parentheses. 
                Returns an empty list if n is 0.
        """
        # filter out erroneous inputs
        if n < 0:
            raise ValueError()
        if not isinstance(n, int):
            raise TypeError()
        
        # exit early for values of n that only have 1 solution
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        
        # list to store results of recursion
        out = []
        
        # build all possible valid strings (every valid entry will start with '(', so current will start off with an open)
        self.gen_next_parentheses(1, 0, "(", n, out)
        
        # after recursion, add a closed to each result and return the list
        for i in range(len(out)):
            out[i] += ')'
        return out
@pytest.mark.parametrize("n, expected", [
    (0, [""]),  # edge case: n = 0
    (1, ["()"]),  # edge case: n = 1
    (2, ["(())", "()()"]),  # happy path: n = 2
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),  # happy path: n = 3
    (4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]),  # happy path: n = 4
], ids=[
    "n=0",
    "n=1",
    "n=2",
    "n=3",
    "n=4"
])
def test_generateParenthesis(n, expected):
    # Act
    result = Solution().generateParenthesis(n)

    # Assert
    assert result == expected

@pytest.mark.parametrize("n", [
    (-1),  # error case: negative number
    (1.5),  # error case: non-integer
    ("a"),  # error case: non-numeric
], ids=[
    "negative_number",
    "non_integer",
    "non_numeric"
])
def test_generateParenthesis_invalid_input(n):
    # Act & Assert
    with pytest.raises((TypeError, ValueError)):
        Solution().generateParenthesis(n)
        
if __name__ == "__main__":
    print(Solution().test())
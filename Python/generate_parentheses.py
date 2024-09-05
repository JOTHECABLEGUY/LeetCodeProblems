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
import random
from typing import List
class Solution:
    def test(self):
        return self.generateParenthesis(3)
    
    def gen_next_parentheses(self, open_count, closed_count, curr, n, out):
        # base case: exit when number of closed = number of open = the requested number of pairs
        # if open_count == closed_count == n:
        #     out.append(curr)
        #     return
        if open_count + closed_count == n*2 - 1:
            out.append(curr)
            return 
        # can only add ( if number of open parentheses is below number of pairs requested
        if open_count < n:
            curr += '('
            self.gen_next_parentheses(open_count+1, closed_count, curr, n, out)
            curr = curr[:-1]
        
        # can only add ) if number of closed parentheses is below number of open parentheses
        if closed_count < open_count:
            curr += ')'
            self.gen_next_parentheses(open_count, closed_count+1, curr, n, out)
            curr = curr[:-1]
            
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        self.gen_next_parentheses(0, 0, "", n, out)
        for i in range(len(out)):
            out[i] += ')'
        return out
if __name__ == "__main__":
    print(Solution().test())
"""440. K-th Smallest in Lexicographical Order
Hard
Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].


Example 1:

Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.
Example 2:

Input: n = 1, k = 1
Output: 1

Constraints:

1 <= k <= n <= 109"""

import pytest

class Solution:
    
    def test(self): return (self.findKthNumber(2, 2))
    
    def findKthNumber(self, n: int, k: int) -> int:
        if k < 2: return k
        if k == n:
            return n if k %10 else n-1
        lex_order = []
        def dfs(current):
            if current > n: return
            lex_order.append(current)
            for i in range(10):
                new_num = 10 * current + i
                if new_num > n: return
                dfs(new_num)
        for i in range(1, n):
            dfs(i)
        return lex_order[k-1]
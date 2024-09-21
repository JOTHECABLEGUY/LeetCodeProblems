"""386. Lexicographical Numbers
Medium
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 


Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]

Constraints:

1 <= n <= 5 * 104"""

from typing import List
import pytest

class Solution():
    
    def test(self): return self.lexicalOrder(13)
    
    def lexicalOrder(self, n:int) -> List:
        
        # initialize the return list, return early if n is not valid
        lexOrder = []
        if n < 1: return lexOrder
        
        # recursive helper method to dig down into the prefix tree and add elements to the return list
        def dfs(current):
            
            # return when base case is met, input is above the limit
            if current > n: return
            
            # add the input to the list
            lexOrder.append(current)
            
            # progressively build longer numbers to step down, stop if the numbers go above the limit
            for i in range(10):
                check_next = current *10 + i
                if check_next > n: return
                
                # recursively build more numbers
                dfs(check_next)
        
        # call the recursive helper for each single digit  
        for i in range(1, 10):
            dfs(i)

        # return the list built by the helper function
        return lexOrder

@pytest.mark.parametrize("n, expected", [
    # Happy path tests
    (1, [1]),  # Single digit
    (10, [1, 10, 2, 3, 4, 5, 6, 7, 8, 9]),  # Two digits
    (13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]),  # Small number

    # Edge cases
    (0, []),  # Zero case
    (9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),  # Single digit upper limit
    (100, [1, 10, 100, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 6, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 7, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 8, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 9, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]),  # Three digits

    # Error cases
    (-1, []),  # Negative number
], ids=[
    "single_digit",
    "two_digits",
    "small_number",
    "zero_case",
    "single_digit_upper_limit",
    "three_digits",
    "negative_number"
])
def test_lexicalOrder(n, expected):

    # Act
    result = Solution().lexicalOrder(n)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
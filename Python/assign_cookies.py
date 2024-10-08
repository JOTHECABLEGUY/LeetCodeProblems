"""455. Assign Cookies
Easy
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.


Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

Constraints:

1 <= g.length <= 3 * 104
0 <= s.length <= 3 * 104
1 <= g[i], s[j] <= 231 - 1"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.findContentChildren([10, 9, 8], [5, 6, 7])
    
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        # return early if one of the inputs is empty
        if not (g and s):
            return 0
        
        # sort both input lists
        g.sort()
        s.sort()
        
        # create pointers for positions in s and g, as well as a counter for number of content children
        g_p, s_p, count = 0,0,0
        
        # while there are still elements to compare
        while g_p < len(g) and s_p < len(s):
            
            # if the current greed can be satisfied by the current cookie size (greed is <= size),
            #   increment counter and greed pointer
            if g[g_p] <= s[s_p]:
                count += 1
                g_p += 1
            
            # increment size pointer
            s_p += 1
        
        # return number of content children
        return count

@pytest.mark.parametrize(
    "g, s, expected",
    [
        # Happy path tests
        ([1, 2, 3], [1, 1], 1),  # ID: happy_path_1
        ([1, 2], [1, 2, 3], 2),  # ID: happy_path_2
        ([1, 2, 3], [3], 1),     # ID: happy_path_3

        # Edge cases
        ([], [], 0),             # ID: edge_case_empty_lists
        ([1, 2, 3], [], 0),      # ID: edge_case_no_cookies
        ([], [1, 2, 3], 0),      # ID: edge_case_no_children
        ([1], [1], 1),           # ID: edge_case_single_child_single_cookie

        # Error cases
        ([1, 2, 3], [0, 0, 0], 0),  # ID: error_case_no_sufficient_cookies
        ([10, 9, 8], [5, 6, 7], 0), # ID: error_case_large_greedy_values
    ]
)
def test_findContentChildren(g, s, expected):
    # Act
    result = Solution().findContentChildren(g, s)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
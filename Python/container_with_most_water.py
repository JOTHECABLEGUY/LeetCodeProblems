"""11. Container With Most Water
Medium
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4"""
from typing import List
import pytest
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for x1, y1 in enumerate(height):
            for x2, y2 in enumerate(height):
                max_area = max(max_area, min(y1, y2)*(x2-x1))
        return max_area
    def maxArea_2(self, height:List[int]) -> int:
        if len(height) in {0, 1}:
            return 0
        l, r, max_a = 0, len(height)-1, 0
        while l < r:
            l_height, r_height = height[l], height[r]
            max_a = max(max_a, (r-l) * min(l_height, r_height))
            if l_height < r_height:
                l += 1
                while l < r and height[l] < l_height:
                    l += 1
            else:
                r -= 1
                while r > l and height[r] < r_height:
                    r -= 1
        return max_a
    def maxArea_3(self, height:List[int])->int:
        max_a, l, r = 0, 0, len(height)-1
        while l < r:
            max_a = max(max_a, (r-l)*min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_a
    def test(self):
        return self.maxArea_3([1, 2, 4, 3])
@pytest.mark.parametrize("height, expected", [
    # Happy path tests
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),  # ID: typical case
    ([1, 1], 1),  # ID: minimal case
    ([4, 3, 2, 1, 4], 16),  # ID: symmetrical case
    ([1, 2, 1], 2),  # ID: small case

    # Edge cases
    ([1], 0),  # ID: single element
    ([1, 2], 1),  # ID: two elements
    ([1000, 1000, 1000, 1000, 1000], 4000),  # ID: large values

    # Error cases
    ([], 0),  # ID: empty list
], ids = ["typical case", "minimal case", "symmetrical case", "small case", "single element",
        "two elements", "large values", "empty list"])
def test_maxArea(height, expected):
    # Act
    result = Solution().maxArea_3(height)

    # Assert
    assert result == expected
if __name__ == "__main__":
    print(Solution().test())
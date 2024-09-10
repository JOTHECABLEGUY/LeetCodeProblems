"""303. Range Sum Query - Immutable
Easy
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange."""

import pytest
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.data = nums
        n = len(nums)
        self.cache = {}
        for i, num in enumerate(nums):
            self.cache[i] = [num]
        for start in range(n):
            for end in range(start+1, n):
                self.cache[start].append(self.cache[start][-1] + nums[end])

    def sumRange(self, left: int, right: int) -> int:
        if left < 0 or right >= len(self.data) or left > right or left > len(self.data):
            raise IndexError
        return self.cache[left][right-left]

def t():
    obj = NumArray([-2,0,3,-5,2,-1])
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    return obj.sumRange(0, 5)


obj = NumArray([1, 2, 3, 4, 5])
class TestSumRange:

    @pytest.mark.parametrize("left, right, expected", [
        (0, 2, 6),  # happy path
        (1, 3, 9),  # happy path
        (0, 4, 15),  # happy path
        (2, 2, 3),  # edge case: single element
        (0, 0, 1),  # edge case: single element
        (4, 4, 5),  # edge case: single element
    ], ids=[
        "sum_0_to_2",
        "sum_1_to_3",
        "sum_0_to_4",
        "sum_2_to_2",
        "sum_0_to_0",
        "sum_4_to_4",
    ])
    def test_sum_range(self, left, right, expected):
        
        # Act
        result = obj.sumRange(left, right)
        
        # Assert
        assert result == expected

    @pytest.mark.parametrize("left, right, expected", [
        (0, 2, 6),  # cache hit
        (1, 3, 9),  # cache hit
    ], ids=[
        "cache_hit_0_to_2",
        "cache_hit_1_to_3",
    ])
    def test_sum_range_cache(self, left, right, expected):
        
        # Arrange
        obj.sumRange(left, right)  # populate cache
        
        # Act
        result = obj.sumRange(left, right)
        
        # Assert
        assert result == expected

    @pytest.mark.parametrize("left, right", [
        (-1, 2),  # error case: negative index
        (1, 5),  # error case: right index out of bounds
        (5, 5),  # error case: left index out of bounds
        (3, 2),  # error case: left > right
    ], ids=[
        "negative_index",
        "right_index_out_of_bounds",
        "left_index_out_of_bounds",
        "left_greater_than_right",
    ])
    def test_sum_range_errors(self, left, right):
        
        # Act & Assert
        with pytest.raises(IndexError):
            obj.sumRange(left, right)

if __name__ == "__main__":
    print(t())


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
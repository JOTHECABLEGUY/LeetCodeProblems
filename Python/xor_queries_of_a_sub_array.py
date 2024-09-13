"""1310. XOR Queries of a Subarray
Medium
You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.


Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]

Constraints:

1 <= arr.length, queries.length <= 3 * 104
1 <= arr[i] <= 109
queries[i].length == 2
0 <= lefti <= righti < arr.length"""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.xorQueries([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]])
    
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        """
            Computes the XOR of elements in specified subarrays of a given array.

            This function takes an array and a list of queries, where each query specifies a range of indices. 
            It returns a list of results, each representing the XOR of the elements in the specified range.

            Args:
                arr (List[int]): The input array of integers.
                queries (List[List[int]]): A list of queries, where each query is a list containing two integers 
                                            representing the start and end indices of the subarray.

            Returns:
                List[int]: A list of integers where each integer is the result of the XOR operation 
                            for the corresponding query.
        """
        
        # start prefix list with the first element of arr
        prefix = [arr[0]]
        
        # finish prefix array by xor on current element in arr with prefix of the previous element
        prefix.extend(prefix[i-1]^arr[i] for i in range(1, len(arr)))
        
        # return result such that the ith entry is the answer to the ith query in queries
        #   its built by taking the left and right bounds from the current query, and if the left
        #   bound is 0, the entry will just be the prefix of the right bound, otherwise the entry
        #   will be the prefix of the right bound xor the prefix of the element before the left bound
        return [prefix[q[1]]^prefix[q[0]-1] if q[0] else prefix[q[1]] for q in queries]

@pytest.mark.parametrize(
    "arr, queries, expected",
    [
        # Happy path tests
        ([1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]], [2, 7, 14, 8]),
        ([4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 2]], [8, 0, 4, 14]),
        
        # Edge cases
        ([0], [[0, 0]], [0]),
        ([1, 1, 1, 1], [[0, 3], [1, 2]], [0, 0]),
        ([1, 2, 3, 4], [[0, 0], [1, 1], [2, 2], [3, 3]], [1, 2, 3, 4]),
        
        # Error cases
        ([], [], []),
        ([1, 2, 3], [], []),
    ],
    ids=["happy_path_1", "happy_path_2", "single_element", "all_same_elements", 
        "single_element_queries", "empty_arrays", "empty_queries"]
)
def test_xorQueries(arr, queries, expected):

    # Act
    result = Solution().xorQueries(arr, queries)

    # Assert
    assert result == expected
    
if __name__ == "__main__":
    print(Solution().test())
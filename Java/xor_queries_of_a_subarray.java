
import java.util.Arrays;

/*1310. XOR Queries of a Subarray
Solved
Medium
Topics
Companies
Hint
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
0 <= lefti <= righti < arr.length */

class Solution {

    /*
        method to perform xor on subarrays of an array given the subarrays' bounds
        @param arr (int[]): array of integers to perform xor on
        @param queries (int[][]): array of pairs of integers representing bounds of subarrays
            to perform the xor over
        @returns int[]: an array such that answer[i] is the result of the ith query in queries
    */
    public int[] xorQueries(int[] arr, int[][] queries) {

        // array to store the result of xor from 0 to the ith position in arr
        int[] prefix = new int[arr.length];

        // array to store the results of each query
        int[] answer = new int[queries.length];

        // initialize the first element of prefix to be the first element from arr (result of query {0, 0})
        prefix[0] = arr[0];

        // build the prefix array, each entry is the current element in arr xor the previous xor result in the prefix array
        for (int i = 1; i < arr.length; i++){
            prefix[i] = prefix[i-1]^arr[i];
        }

        // process the queries
        for (int i = 0; i < queries.length; i++){

            // the first index and second index of the query
            int first = queries[i][0];
            int second = queries[i][1];

            // if first is 0, the prefix array already has the requested answer, so we take it from there
            if (first == 0) answer[i] = prefix[second];

            // otherwise, xor the prefix of the second value (right bound) with the prefix of the 
            //      element before the first value (left bound). e.g. [2, 3] is the same as [0, 3]^[0, 1]
            else answer[i] = prefix[second]^prefix[first-1];
        }
        return answer;
    }
    public static void main(String args[]){
        Solution obj = new Solution();
        int[] arr = {1, 3, 4, 8};
        int[][] qs = {{0, 1}, {1, 2}, {0, 3}, {3, 3}};
        int[] ans = obj.xorQueries(arr, qs);
        System.out.println(Arrays.toString(ans));
    }
}

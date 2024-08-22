#include <string>
#include <iostream>
#include <vector>
using namespace std;
class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {

        vector<int> map(256, -1); // map to store chars and their indices. yields -1 if not in the map
        int left = 0, right = 0;  // left and right pointers to capture substrings
        int max_dist = 0;         // stores the maximum length of a substring without repeating chars
        int n = s.size();         // stopping point of loop

        // traverse the string
        while (right < n)
        {
            char curr_char = s[right];
            int val = map[curr_char];

            // if char in map, need to jump left index
            // (dont need to jump left index if the map value is out of subwindow range)
            if (val != -1)
            {
                left = max(val + 1, left); // if jumping, set index to 1 more than repeated char
            }

            map[curr_char] = right;                     // update the index of the char in the map
            max_dist = max(max_dist, right - left + 1); // update max distance if a longer substring was found
            right++;                                    // inc right pointer
        }
        return max_dist; // return max distance after traversal
    }
};
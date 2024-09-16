/*539. Minimum Time Difference
Medium
Topics
Companies
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM". */

import java.util.*;

class Solution {
    public int findMinDifference(List<String> timePoints) {
        int hour24 = 24*60;
        if(timePoints.size() >= hour24) return 0;
        boolean[] seen = new boolean[hour24];
        for (String s:timePoints){
            int t = extractMinutes(s);
            if (seen[t]) return 0;
            seen[t] = true;
        }

        int minDiff = Integer.MAX_VALUE;
        int firstIndex = Integer.MAX_VALUE;
        int prevIndex = Integer.MAX_VALUE;

        for (int index = 0; index < hour24; index++){
            if(seen[index]){
                if(firstIndex == Integer.MAX_VALUE) firstIndex = index;
                else minDiff = Math.min(minDiff, index - prevIndex);
                prevIndex = index;
            }
        }
        minDiff = Math.min(minDiff, hour24 + firstIndex - prevIndex);
        return minDiff;
    }

    private static int extractMinutes(String s){
        return ((s.charAt(0) - '0')*10 + s.charAt(1)-'0')*60 + (s.charAt(3)-'0')*10 + s.charAt(4) - '0';
    }

    public static void main(String[] args){
        Solution obj = new Solution();
        String[] arr = {"00:00","23:59"};
        List<String> tp = new ArrayList<>(Arrays.asList(arr));
        System.out.println(obj.findMinDifference(tp));
    }
}

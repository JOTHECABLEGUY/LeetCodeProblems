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

        HashMap<String, Integer> hash = new HashMap<>();
        int minDiff = Integer.MAX_VALUE;
        int hour24 = 24*60;
        int diff, end;
        for (String s: timePoints){
            if(!hash.containsKey(s)) hash.put(s, extractMinutes(s));
        }

        for (int start = 0; start < timePoints.size(); start++){
            for (end = start+1; end < timePoints.size(); end++){
                diff = Math.abs(extractMinutes(timePoints.get(end)) - extractMinutes(timePoints.get(start)));
                minDiff = Math.min(minDiff, Math.min(diff, hour24 - diff));
                if (minDiff == 0) return 0;
            }
        }
        return minDiff;
    }

    private static int extractMinutes(String s){
        String[] spl = s.split(":");
        return Integer.parseInt(spl[0])*60 + Integer.parseInt(spl[1]);
    }

    public static void main(String[] args){
        Solution obj = new Solution();
        String[] arr = {"00:00","23:59"};
        List<String> tp = new ArrayList<>(Arrays.asList(arr));
        System.out.println(obj.findMinDifference(tp));
    }
}

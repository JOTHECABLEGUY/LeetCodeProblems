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
    /**
     * Method to find the minimum difference between any two timestamps in list expressed in minutes
     * @param timePoints (String[]): List of timestamps of the form "HH:MM", zero-padded
     * @return int: minimum difference between any two timestamps in the input list
     */
    public int findMinDifference(List<String> timePoints) {

        // number of minutes in 24 hours
        final int hour24 = 24*60;

        // if there are more points than possible combinations, there must be at least 
        //  1 duplicate in the list, thus making the minimum difference 0
        if(timePoints.size() >= hour24) return 0;

        // array to store whether a timestamp was seen
        boolean[] seen = new boolean[hour24];

        // loop through the timestamps and populate the seen array. If a value was seen before, 
        //  return 0 as a duplicate was found.
        for (String s:timePoints){
            int t = extractMinutes(s);
            if (seen[t]) return 0;
            seen[t] = true;
        }

        // minimum tim difference in minutes
        int minDiff = Integer.MAX_VALUE;

        // index of first timestamp from the input array with respect to the seen array
        int firstIndex = Integer.MAX_VALUE;

        // index of previous timestamp from the input array with respect to seen array
        int prevIndex = Integer.MAX_VALUE;

        // loop through the seen array
        for (int index = 0; index < hour24; index++){

            // only need to process timestamps that occur in the input array
            if(seen[index]){

                // set the index of the first element from the input array
                if(firstIndex == Integer.MAX_VALUE) firstIndex = index;

                // if it is not the first element, update the minimum difference if the current
                //  timestamp - previously seen timestamp is below the current min
                else minDiff = Math.min(minDiff, index - prevIndex);

                // regardless of the above checks, update the previous index
                prevIndex = index;
            }
        }

        // after the array has been traversed, we still need to check the boundary where 23:59 
        //  crosses back into the 00:00 territory. We take the minimum of the current min and
        //  the number of minutes in a day - the previous timestamp (highest minute value) + 
        //  the first Index (lowest minute value). This ensures that the number of minutes between
        // the numbers closest to 24:00/00:00 from the left and right is accounted for 
        minDiff = Math.min(minDiff, hour24 + firstIndex - prevIndex);
        
        // return the minimum number of minutes between pairs of timestamps in the input array
        return minDiff;
    }

    /**
     * Method to convert a String timestamp in the form "HH:MM" to a number of minutes after 00:00
     * @param s (String): String to convert to minutes
     * @return int: number of minutes equivalent to the input "HH:MM" timestamp
     */
    private static int extractMinutes(String s){

        // get the chars at each significant index and subtract the char '0' to get their ordinal value
        //  then multiply by 10 if the digit is in the 10s place. Multiply the Hour portion by 60 to get
        //  the number of minutes in the hours and add the hours-as-minutes and the minutes to get the total
        return ((s.charAt(0) - '0')*10 + s.charAt(1)-'0')*60 + (s.charAt(3)-'0')*10 + s.charAt(4) - '0';
    }

    public static void main(String[] args){
        Solution obj = new Solution();
        String[] arr = {"00:00","23:59"};
        List<String> tp = new ArrayList<>(Arrays.asList(arr));
        System.out.println(obj.findMinDifference(tp));
    }
}

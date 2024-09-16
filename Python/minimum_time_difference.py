"""539. Minimum Time Difference
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
timePoints[i] is in the format "HH:MM"."""

import pytest
from typing import List

class Solution:
    
    def test(self):
        return self.findMinDifference(["12:59", "13:59"])
    
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) < 2:
            return 0
        hours_24 = 24*60

        seen = set()

        for tp in timePoints:
            h = int(tp[:2])
            m = int(tp[3:])
            if h > 23 or m > 59:
                raise ValueError
            mins = h*60 + m
            if mins in seen: return 0
            seen.add(mins)

        seen = sorted(seen)

        min_diff = hours_24 + seen[0] - seen[-1]

        for i in range(len(seen)-1):
            if seen[i+1] - seen[i] < min_diff:
                min_diff = seen[i+1] - seen[i]

        return min_diff

@pytest.mark.parametrize("timePoints, expected, _id", [
        (["23:59", "00:00"], 1, "midnight_edge_case"),
        (["01:01", "02:02", "03:03"], 61, "sequential_times"),
        (["00:00", "12:00", "23:59"], 1, "full_day_edge_case"),
        (["05:31", "22:08", "00:35"], 147, "random_times"),
        (["00:00", "00:00"], 0, "duplicate_times"),
        
        ([], 0, "empty_list"),
        (["00:00"], 0, "single_time_point"),
        (["12:30", "12:30", "12:30"], 0, "multiple_duplicates"),
    ])
def test_find_min_difference(timePoints, expected, _id):

    # Act
    result = Solution().findMinDifference(timePoints)

    # Assert
    assert result == expected, f"test failed on {_id}"

@pytest.mark.parametrize("timePoints, expected_exception", [
    (["00:00", "24:00"], ValueError),
    (["12:60", "00:00"], ValueError),
])
def test_find_min_difference_error_cases(timePoints, expected_exception):

    # Act and Assert
    with pytest.raises(expected_exception):
        Solution().findMinDifference(timePoints)

if __name__ == "__main__":
    print(Solution().test())
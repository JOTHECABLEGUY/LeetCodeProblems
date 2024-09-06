"""207. Course Schedule
Medium
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique."""

import pytest
from typing import List
class Solution:
    def test(self):
        return self.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])
    def dfs(self, adj_map, course, visited_set):
        if course in visited_set:
            return False
        if not adj_map[course]:
            return True
        visited_set.add(course)
        for prereq in adj_map[course]:
            if course == prereq:
                return False
            if not self.dfs(adj_map, prereq, visited_set):
                return False
        adj_map[course] = []
        visited_set.remove(course)
        return True
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0:
            return False
        prerequisites = [x for x in prerequisites if x]
        if len(prerequisites) <= 1:
            return True
        courses = range(numCourses)
        visited = set()
        adj_map = {c: [] for c in courses}
        for course, prereq in prerequisites:
            adj_map[course].append(prereq)
        return all(self.dfs(adj_map, course, visited) for course in range(numCourses))
    
@pytest.mark.parametrize(
    "numCourses, prerequisites, expected",
    [
        # Happy path tests
        (2, [[1, 0]], True),
        (4, [[1, 0], [2, 1], [3, 2]], True),
        (3, [[0, 1], [1, 2]], True),
        
        # Edge cases
        (0, [], False),
        (1, [], True),
        (2, [], True),
        (2, [[1, 0], [0, 1]], False),
        (3, [[0, 1], [1, 2], [2, 0]], False),
        
        # Error cases
        (2, [[]], True),
        (2, [[1, 0], []], True),
    ],
    ids=["single_prerequisite", "linear_dependencies", "simple_chain", "no_courses", "single_course_no_prerequisites",
         "two_courses_no_prerequisites", "circular_dependency", "circular_dependency_three_courses",
         "empty_prerequisite_list", "mixed_empty_and_non_empty_prerequisites"]
)
def test_canFinish(numCourses, prerequisites, expected):

    # Act
    result = Solution().canFinish(numCourses, prerequisites)

    # Assert
    assert result == expected

if __name__ == "__main__":
    print(Solution().test())
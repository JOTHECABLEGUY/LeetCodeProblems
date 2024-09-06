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
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
            Determines if all courses can be completed given the number of courses and their prerequisites.

            This function checks for cycles in the course prerequisite graph using depth-first search (DFS). 
            If a cycle is detected, it returns False; otherwise, it returns True indicating all courses can be completed.

            Args:
                numCourses (int): The total number of courses.
                prerequisites (List[List[int]]): A list of prerequisite pairs where each pair [a, b] indicates that 
                                                course a depends on course b.

            Returns:
                bool: True if all courses can be finished, False otherwise.
        """
        
        # exit if there are no courses to take
        if numCourses <= 0:
            return False
        
        # filter out empty prereqs lists
        prerequisites = [x for x in prerequisites if x]
        
        # if only one prereq is required, return True
        if len(prerequisites) <= 1:
            return True
        
        # build of list of courses, starting at 0
        courses = range(numCourses)
        
        # set to store list of visited nodes (detect cycle)
        visited = set()
        
        # initialize each course with a list of prereqs required
        adj_map = {c: [] for c in courses}
        
        # add each prerequisite to the corresponding course's list
        for course, prereq in prerequisites:
            adj_map[course].append(prereq)
        
        
        def dfs(course:int):
            """
                Performs a depth-first search to determine if the given course can be completed.

                This function checks for cycles in the prerequisite graph by tracking visited courses. 
                If a cycle is detected or a course has a prerequisite that cannot be completed, it returns False; 
                otherwise, it returns True indicating the course can be completed.

                Args:
                    course (int): The course to check for completion.

                Returns:
                    bool: True if the course can be completed, False otherwise.
            """
            
            # if the course has already been seen, a cycle exists, return False
            if course in visited:
                return False
            
            # if there are no prerequisites that need to be traversed, return True
            if not adj_map[course]:
                return True
            
            # add the current course to the visited set
            visited.add(course)
            
            # use depth-first search to check if each prerequisite can be finished (if all prereqs can be completed,
            # the course can also be completed). If any prereqs cannot be completed or the prereq is the course itself, 
            # return False
            for prereq in adj_map[course]:
                if course == prereq or not dfs(prereq):
                    return False
                
            # if all prereqs can be finished, set the prereq list as empty so any checks on the course will reflect the lack of blockers
            adj_map[course] = []
            
            # remove the course from visited: the course can be completed, but may be checked by other courses:
            #   this allows for backtracking
            visited.remove(course)
            return True
        
        # return True if all provided prereqs can be met (meaning all courses can be finished)
        return all(dfs(course) for course in range(numCourses))
    
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
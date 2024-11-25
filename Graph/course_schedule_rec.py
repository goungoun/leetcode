# 207. Course Schedule (Medium)
# https://leetcode.com/problems/course-schedule

from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Check all the course prerequisits do not have a cycle
        return True (if we can finish all courses)

        Example 1:
        prerequisites = [[1,0]]
        1 -> 0
        return True

        Example 2:
        prerequisites = [[1,0],[0,1]]
        1 <=> 0, a cycle
        return False

        Approach:
        DFS to see if there is a cycle for a course
        Repeat the cycle dection for all the courses
        For optimization, once the course is validated make it empty prerequisits
        """

        if not prerequisites: # prerequisites is None or len(prerequisites) == 0
            return True
        
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        visiting = set()

        def cycle(course):
            """
            return True if there is a cycle
            """
            if course in visiting:
                return True

            visiting.add(course)

            for pre in graph[course]:
                if cycle(pre):
                    return True

            visiting.remove(course)
            graph[course] = [] # no duplicate chk

            return False

        # chk all courses do not have a cycle
        for i in range(numCourses):
            if cycle(i):
                return False
        
        # can finish
        return True

# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii

# Warning!!!!! It does not pass the test case. Need to deal with a cycle detection or consider to apply Khan's algorithm (BFS)
# numCourses = 2, prerequisites = [[0,1],[1,0]]
# output [1,0]
# expected []

from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        schedule = []
        taken = set()

        g = defaultdict(list)

        # to take the course, must take other prep courses
        for course, prep in prerequisites:
            g[course].append(prep)

        def can_finish(course):
            if course in taken:
                return

            taken.add(course)

            # take pre course
            for prep in g[course]:
                if prep not in taken:
                    can_finish(prep)

            # and then add the course to the schedule        
            schedule.append(course)
            return

        for course in range(numCourses):
            can_finish(course)

        return schedule

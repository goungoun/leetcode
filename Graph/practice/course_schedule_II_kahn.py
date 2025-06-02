# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/

# This code does not pass the cycle case
# prerequisites = [[1,0],[1,2],[0,1]], numCourses = 3

from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        BFS, incomming count check
        """
        course_order = []

        # build outgoing graph & incoming count
        g = defaultdict(list)
        in_count = [0] * numCourses

        for course, pre in prerequisites:
            g[pre].append(course)
            in_count[course] += 1

        q = deque([])
      
        # courses without prerequsite
        for i, cnt in enumerate(in_count):
            if cnt == 0:
                q.append(i)

        # not possible to finish the course
        if not q:
            return []

        taken = set()
        while q:
            pre = q.popleft()
            taken.add(pre)
            course_order.append(pre)

            # update in_count
            for course in g[pre]:
                in_count[course] -= 1
                if in_count[course] == 0 and course not in taken:
                    q.append(course)

        return course_order # Fix This: if cycle return []

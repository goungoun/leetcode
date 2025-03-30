# 210. Course Schedule II
# https://leetcode.com/problems/course-schedule-ii

from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Topological sort to finish all courses
        return course_order (or empty list if you cannot finish)

        Example 1: Can finish
        numCourses = 2, prerequisites = [[1,0]]

        1 -> 0

        return [0, 1]

        Example 2: Can finish
        numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]

        - 3 -> 1 -> 0 <- 2 <- 3 -
        0, (1,2), 3
        
        return [0,1,2,3] (or [0,2,1,3])

        Example 3: Cannot finish
        numCourses = 4, prerequisites = [[5,6],[6,7],[7,5]]

        return []

        Approach: Kahn's algorithm, BFS
        Start with in-degree 0 classes that no prerequsites are required
        Check the next courses and decrease the in-degree
        Check another in-degree 0 classes after the update and repeat until all courses are taken
        """
        if not numCourses or not 1 <= numCourses <= 2000:
            raise ValueError(f"1 <= numCourses <= 2000, numCourses={numCourses}")

        course_order = []
        in_degree = [0] * numCourses

        # build a direcitonal graph : pre -(next)-> course & accumulate in-degree
        g = defaultdict(list)
        for course, pre in prerequisites:
            g[pre].append(course)
            in_degree[course] += 1

        q = deque()

        # we can start from all courses with in-degree 0, which means no prerequsite
        for course, cnt in enumerate(in_degree):
            if cnt == 0:
                q.append(course)
                
        while q:
            course = q.popleft() # BFS
            course_order.append(course)

            # next course
            for next_course in g[course]:
                in_degree[next_course] -= 1

                # add in-degree 0 to the queue
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        return course_order if len(course_order) == numCourses else []

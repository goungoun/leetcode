# 207. Course Schedule (Medium)
# https://leetcode.com/problems/course-schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses is None:
            return False

        g = defaultdict(list)
        for ai, bi in prerequisites:
            g[ai].append(bi)

        def finish(course):
            if taking[course]:
                return False
            
            taking[course] = True

            for pre in g[course]:
                if not finish(pre):
                    return False

            taking[course] = False
            # g[course] = [] # Here!! Uncomment it to prevent Time Limit Exceed (100 courses)

            return True

        for i in range(0, numCourses):
            taking = [False]*numCourses
            if not finish(i):
                return False

        return True

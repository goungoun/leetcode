# 210. Course Schedule II (Medium)
# https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Sort courses to finish all courses (Topological sort)
        return course_order

        Example 1: numCourses = 2
        prerequisites = [[1,0]]
        1 -> 0
        return [0, 1]

        Example 2: numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        3 -> 1 or 2 -> 0 
        return [0, 1, 2, 3] or [0, 2, 1, 3]

        Example 3: numCourses = 1
        prerequisites = []
        return [0]

        Approach: DFS
        Build a graph, key:value = {course:[prerequisites]}
        Traverse a graph until the course does not have the prerequisites
        If any cycle is detected just return empty list, otherwise append a course to the course order list

        Beats 90.31%, T=O(V+E)
        """
        graph = defaultdict(list)

        for course, pre in prerequisites:
            graph[course].append(pre)
        
        course_status = [''] * numCourses
        course_order = []

        def is_cycle(course):
            """
            It updates a course_status and a course_order
            return True if there is a cycle
            """
            prv_status = course_status[course]
            if prv_status == 'START':
                return True
            
            course_status[course] = 'START'
            
            for pre in graph[course]:
                if is_cycle(pre):
                    return True
            
            course_status[course] = 'END'

            graph[course] = [] # no duplicate chk

            if prv_status == '':
                course_order.append(course)

            return False

        for i in range(numCourses):
            # If there is a cycle, we cannot finish the courses
            if is_cycle(i):
                return []
        
        return course_order

# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

from heapq import heappop, heappush
class Solution:
    """
    Connect all points with the minimum distance
    return min_dist

    * manhattan distance :|xi - xj| + |yi - yj|

    Example 1:
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    [0,0]~[2,2]: 2 + 2 = 4
    [2,2]~[3,10]: 1 + 8 = 9
    [2,2]~[5,2]: 3 + 0 = 3
    [5,2]~[7,0]: 2 + 2 = 4

    4 + 9 + 3 + 4 = 20

    return 20

    Approach: Minimum Spanning Tree
    Start with an any point and make a group
    Expand the group by adding a nearest point which is greedy
    Repeat until the group includes all points
    """
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        n = len(points)
        min_cost = 0
        h = [(0,0)] # dist, idx of points
        group = set()

        # O(ElogV)
        while len(group) < n: 
            dist, i = heappop(h) # nearest from the group
            if i not in group:
                group.add(i)
                min_cost += dist
                xi, yi = points[i]

                # points ordered by the distance
                for j in range(n):
                    if j not in group:
                        xj, yj = points[j]
                        manhattan_dist = abs(xi-xj) + abs(yi-yj)
                        heappush(h, (manhattan_dist, j))

        return min_cost
        
# Reference: Gregg Hog
        

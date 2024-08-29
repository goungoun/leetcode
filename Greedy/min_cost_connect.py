# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Optimize cost connecting all points with the minimum distance
        return min_cost

        * Manhattan distance (=cost) :|xi - xj| + |yi - yj|

        Approach: Minimum Spanning Tree (Prim)
        Start with an any point and make a group
        Expand the group by adding a nearest point, which is greedy
        Repeat until the group includes all points
        """

        n = len(points)
        min_cost = 0
        min_heap = [(0,0)] # dist, idx of points
        group = set()

        # O(ElogV)
        while len(group) < n:
            # nearest 
            dist, i = heappop(min_heap)

            if i not in group:
                group.add(i)
                min_cost += dist
                xi, yi = points[i]

                # points order using heap
                for j in range(n):
                    if j not in group:
                        xj, yj = points[j]
                        manhattan_dist = abs(xi-xj) + abs(yi-yj)
                        heappush(min_heap, (manhattan_dist, j))

        return min_cost
        
# Reference: Gregg Hog
        

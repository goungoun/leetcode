# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/

from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        h = [] # min heap
        ret = []

        for x,y in points:
            d = sqrt( (x*x) + (y*y))
            heappush(h, (d, (x,y)))

        for i in range(k):
            p = heappop(h)
            ret.append(p[1])

        return ret

# 1051. Height Checker
# https://leetcode.com/problems/height-checker/

from heapq import heapify, heappop

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        h = heights.copy()
        heapify(h)
      
        cnt = 0
        for i in range(n):
            val = heappop(h)
            if heights[i] != val:
                cnt += 1

        return cnt

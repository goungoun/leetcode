# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight

from heapq import heapify, heappop, heappush

class MaxHeap:
    """
    Python heap is min heap by default
    The purpose of MaxHeap is to simplify code when max heap is required.
    """
    def __init__(self):
        self.h = []

    def heapify(self, l):
        self.h = [-x for x in l]
        heapify(self.h)

    def heappush(self, value):
        heappush(self.h, -value)

    def heappop(self):
        return -heappop(self.h)

    def len(self):
        return len(self.h)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Pick up heavist two stones and smash them with the following rule
        1) x == y, all destroyed
        2) x != y, x is destroyed and y = y - x

        return weight_last_stone (or 0)

        Example:
        stones = [2,7,4,1,8,1]
        7,8 : [2,-,4,1,8,1] => [2,4,1,1,1]
        2,4 : [-,4,1,1,1] => [2,1,1,1]
        2,1 : [2,-,1,1] => [1,1,1]
        1,1 : [-,-,1] => [1]
        return 1

        Approach:
        Use max heap to pickup the heaviest two stones
        One round, heappop twice and push elements according tho the result
        """
        if not stones:
            return 0
            
        h = MaxHeap()
        h.heapify(stones)

        while h.len() >= 2:
            h.heappush(abs(h.heappop() - h.heappop()))
            
        return h.heappop() if h.len() > 0 else 0




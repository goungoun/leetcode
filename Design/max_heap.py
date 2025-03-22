# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight

from heapq import heapify, heappop, heappush

class MaxHeap:
    """
    Python heap is min heap by default
    The purpose of MaxHeap is to simplify code when max heap is required.
    """
    def __init__(self, iterable=None):
        self._h = [-x for x in iterable] if iterable else []
        heapq.heapify(self._h)

    def heappush(self, value):
        if value is None:
            raise ValueError("Cannot push the empty value to the heap.")
            
        heapq.heappush(self._h, -value)

    def heappop(self):
        if not self._h:
            raise IndexError("The heap is empty. Cannot pop from it")
            
        return -heapq.heappop(self._h)

    def len(self):
        if not self._h:
            return 0
            
        return len(self._h)

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
            
        h = MaxHeap(stones)

        while h.len() > 1:
            w1 = h.heappop()
            w2 = h.heappop()

            diff = abs(w1-w2)
            if diff > 0:
                h.heappush(diff)
            
        return h.heappop() if h.len() > 0 else 0



# 1046. Last Stone Weight
# https://leetcode.com/problems/last-stone-weight

from heapq import heapify, heappop, heappush
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
        Use heap to pickup the heaviest two stones
        Use min heap (by default) like a max heap by making negative values in each element
        One round, heappop twice and push elements according tho the result

        Beats 97.24%
        """
        if not stones:
            return 0
            
        h = [-x for -x in stones]  # Fix This
        h = heapify(stones) # Fix This
      
        # TypeError: object of type 'NoneType' has no len()
        #  ^^^^^^
        while len(h) >= 2:
            h1 = -heappop(h)
            h2 = -heappop(h)

            if h1 > h2:
                heappush(h, -(h1-h2))
            elif h1 < h2:
                heappush(h, -(h2-h1))

        return h[0] if len(h) > 0 else 0 # Fix This

# See also max heap design: ../Design/max_heap.py

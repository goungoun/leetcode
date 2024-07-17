# 70. Climbing Stairs (Bottom Up)
# https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Ways to reach to the top either 1 or two steps
        return cnt

        Example:
        0: () => 1
        1: (1) => 1
        2: (2) (1,1) => 1+1 = 2
        3: (1,2) (2,1) (1,1,1) => 2+1 = 3
        4: (2,2) (1,1,2) (1,2,1) (2,1,1) (1,1,1,1) => 2+3 = 5

        Approach:
        Bottom-up approach without a recursive call
        Replaced an array or a dictionary for cache with two variables, prv and pprv 
        """

        if n == 0 or n == 1:
            return 1 

        pprv = 1 # n = 0
        prv = 1 # n = 1

        curr = 0
        # T=O(n), S=O(1)
        for i in range(2,n+1):
            curr = pprv + prv
            pprv = prv
            prv = curr

        return curr
       

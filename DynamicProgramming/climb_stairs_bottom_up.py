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
        3: (1,2) (2,1) (1,1,1) => 1+2 = 3
        4: (2,2) (1,1,2) (1,2,1) (2,1,1) (1,1,1,1) => 2+3 = 5

        ..
        Fibonacci Sequence!
        
        Approach:
        Bottom-up approach without recursive calls
        Practically it should faster without many function calls
        Additionaly, we can remove an array or a dictionary for memoization to decrease space complexity as well
        """
        
        if n < 0:
            return 0
       
        pprv = 1 
        prv = 1
        curr = 1

        # T=O(n), S=O(1)
        for i in range(2,n+1):
            curr = pprv + prv
            pprv = prv
            prv = curr

        return curr
       

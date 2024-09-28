# 70. Climbing Stairs
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
        Bottom-up DP wihout recursive calls
        Practically it should faster without many function calls
        Additionaly, we can remove an array or a dictionary for memoization to decrease space complexity as well
        """
        if not n or n < 0:
            return 0
    
        pprv, prv, curr = 1, 1, 1

        # T=O(n), S=O(1)
        for i in range(2,n+1):
            curr = pprv + prv
            pprv = prv
            prv = curr

        return curr
    
    def climbStairs_bak(self, n: int) -> int:
        """
        Approach: recursion & memoization
        Design problem with sub problems
        Recurrence Formula: climb(n)= climb(n-2) + climb(n-1)
        Memoize the subproblem result to prevent recomputation by recursive calls
        """
        if n < 1 or n > 45:
            raise ValueError (f"1 <= n <= 45, n={n}")

        memo = [-1]*(n+1)
        memo[0] = 1
        memo[1] = 1

        def rec_climb(n):
            if memo[n] == -1:
                memo[n] = rec_climb(n-2) + rec_climb(n-1)
            return memo[n]

        return rec_climb(n)
    

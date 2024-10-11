# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Ways to reach the top either 1 or two steps
        return cnt

        Example:
        0: () => 1
        1: (1) => 1
        2: (2) (1,1) => 1+1 = 2
        3: (1,2) (2,1) (1,1,1) => 1+2 = 3
        4: (2,2) (1,1,2) (1,2,1) (2,1,1) (1,1,1,1) => 2+3 = 5
        
        ..
        Fibonacci Sequence!
        
        Approach: Bottom-up DP without recursive calls
        Practically it should be faster without many function calls
        Additionally, we can remove an array or a dictionary for memoization to decrease space complexity as well
        """
        if n is None or n < 0:
            return 0
    
        pprv, prv, curr = 1, 1, 1

        # T=O(n), S=O(1)
        for i in range(2,n+1):
            curr = pprv + prv
            pprv = prv
            prv = curr

        return curr

    def climbStairs_bottom_up(self, n: int) -> int:
        """
        Approach: bottom up DP without recursive calls
        Subproblem depends only on solving smaller subproblem
        Memory trade-off, store all computed results and reuse them
        Return the last element of the array
        """
        if n is None or n < 1 or n > 45:
            raise ValueError (f"1 <= n <= 45, n={n}")

        climb = [1]*(n+1)

        # T=O(n), S=O(n)
        for i in range(2,n+1):
            climb[i] = climb[i-2] + climb[i-1]

        return climb[-1]
        
    def climbStairs_top_down(self, n: int) -> int:
        """
        Approach: Top down with memoization
        Design problem with sub problems
        Recurrence Formula, climb(n)= climb(n-2) + climb(n-1)
        Memoize the subproblem result to prevent recomputation by recursive calls
        """
        if n < 1 or n > 45:
            raise ValueError (f"1 <= n <= 45, n={n}")

        memo = [-1]*(n+1)
        memo[0] = 1
        memo[1] = 1

        def climb(n):
            if memo[n] == -1:
                memo[n] = climb(n-2) + climb(n-1)
            return memo[n]

        return climb(n)
    

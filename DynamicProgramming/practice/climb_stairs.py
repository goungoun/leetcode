# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        * n = 1 (1) => 1
        * n = 2 (1, 1) (2) => 2
        n = 3 (1, 2) (1, 1, 1) (2, 1) => 1 + 2 = 3
        n = 4 (1, 1, 2) (2, 2) (1, 2, 1) (1, 1, 1, 1) (2, 1, 1) => 2+3 = 5
        n = 5 ... => 3+5 = 8

        1 2 3 5 8 13 21 ....
        Fibonacci Sequence!!
        Recurrence Formula: climb(n)= climb(n-2) + climb(n-1)
        """
        if n < 1 or n > 45:
            raise ValueError (f"1 <= n <= 45, n={n}")

        memo = ? # complete here #
        memo[0] = ? # complete here #
        memo[1] = 1

        def rec_climb(n):
            if memo[n] == -1:
                # complete here #
            return memo[n]

        return rec_climb(n)
    

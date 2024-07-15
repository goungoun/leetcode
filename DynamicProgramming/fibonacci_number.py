# 508. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        """
        fib(0) = 0
        fib(1) = 1
        fib(n) = fib(n-1) + fib(n-2), for n > 1
        """
        memo = {}
        
        def recfib(n):
            if n <= 1:
                return n
            if n not in memo:
                memo[n] = recfib(n-2) + recfib(n-1)
            return memo[n]

        return recfib(n)

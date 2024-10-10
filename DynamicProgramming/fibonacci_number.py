# 509. Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        """
        Fibonacci sequence, such that each number is the sum of the two preceding ones
        return number

        Example:
        0: 0
        1: 1
        2: 0 + 1 = 1
        3: 1 + 1 = 2
        4: 1 + 2 = 3

        Approach: bottom-up DP
        replace array S=O(n) to variables S=O(1) if all the spaces are not required.      
        """
        if not n or n < 0:
            return 0
        
        pprv, prv, curr = 0, 1, 1

        for i in range(1, n): # Hint: if n=1, range(1,1) does not loop
            curr = pprv + prv
            pprv = prv
            prv = curr
            
        return curr

    def fib_dp(self, n: int) -> int:
        """
        Approach: bottom-up DP
        Rewrite without recursion for better computation and memory use
        T=O(n) beats 99.93%, S=O(n) beats 99.33%
        """
        if not n or n < 0:
            return 0

        f = [0] * (n+1)
        f[1] = 1

        for i in range(2,n+1):
            f[i] = f[i-1] + f[i-2]

        return f[-1]

    def fib_recursive(self, n: int) -> int:
        """
        Fibonacci sequence, such that each number is the sum of the two preceding ones
        return number
        
        Example:
        fib(0) = 0
        fib(1) = 1
        fib(2) = fib(0)+fib(1)
        fib(3) = fib(2)+fib(1)
        fib(4) = fib(3)+fib(2)
        ...
        fib(n) = fib(n-1) + fib(n-2), for n > 1

        Approach: Top-down DP, recursive
        Break down to the sub problem and express a structure of the problem as a recurrence formular. 
        Apply memoization to prevent repetitive calls with the overlapping subproblems
        """
        if not n or n < 0:
            return 0
            
        memo = {}
        
        def recfib(n):
            if n <= 1:
                return n
            if n not in memo:
                memo[n] = recfib(n-2) + recfib(n-1)
            return memo[n]

        return recfib(n)

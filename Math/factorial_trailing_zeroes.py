# 172. Factorial Trailing Zeroes (Medium)
# https://leetcode.com/problems/factorial-trailing-zeroes
from functools import reduce

class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        Calculate n factorial and get the number of zeros at the end of the number
        return cnt_trailing_zeroes

        Example 1:
        n = 3
        3! = 3 x 2 x 1 = 6

        return 0

        Example 2:
        n = 5
        5! = 5 x 4 x 3 x 2 x 1 = 120

        return 1

        Example 3:
        n = 0
        return 0
        """
        if n == 0:
            return 0

        factorial = reduce(lambda a,b: a*b, range(1, n+1), 1)

        cnt = 0
        s = factorial
        while s > 0:
            s, r = divmod(s, 10)
            if r == 0:
                cnt += 1
            else:
                return cnt

        return cnt
        

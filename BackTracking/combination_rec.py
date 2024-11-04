# 77. Combinations (Medium)
# https://leetcode.com/problems/combinations/

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Approach: Pascal's triangle
        C(n,k) = C(n-1, k) + C(n-1, k-1)
        If n is included, k-1 numbers chosen from the range[1, n-1]
        If n is not included, k numbers chosen from the range [1, n-1]

        Beats 5.62%
        """
        if not n or not k:
            return []

        #self.call_cnt = 0
        def bfs(n, k):
            #self.call_cnt += 1
            if k == 1:
                return [[x] for x in range(1, n + 1)]

            if n < k:
                return []

            include_n = bfs(n - 1, k - 1)
            exclude_n = bfs(n - 1, k)
            
            return [x+[n] for x in include_n] + exclude_n

        ret = bfs(n,k)
        #print (f"self.call_cnt={self.call_cnt}, len(ret)={len(ret)}")

        return ret

# referenced and updated semochka(leetcode id:semochka)'s solution
# https://leetcode.com/problems/combinations/solutions/2036326/using-pascal-triangle-to-calculate-combinations/

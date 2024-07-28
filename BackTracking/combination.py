# 77. Combinations (Medium)
# https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        List up the possible combinations on the range [1, n]
        return l_combinations

        Example: 
        n = 4, k = 2
              [1]             [2]       [3]     [4]
        [1,2] [1,3] [1,4] [2,3] [2,4]  [3,4]

        return [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

        Approach:
        To compare permutation, combination ignores the order
        So, for loop range excludes already used numbers
        """
        l_combinations = []
        tmp = []

        def dfs(start):
            if len(tmp) == k:
                l_combinations.append(tmp.copy())
                return
            
            for num in range(start, n + 1):
                tmp.append(num)
                dfs(num + 1)
                tmp.pop()

        dfs(1)
        return l_combinations

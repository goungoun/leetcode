# 72. Edit Distance (Medium)
# https://leetcode.com/problems/edit-distance

class Solution:
    """
    How many operations are required to Insert/Delete/Replace word1 to word2
    return min_ops

    Example 1:
    word1 = "horse", word2 = "ros"
    return 3

    Example 2:
    word1 = "intention", word2 = "execution"
    return 5

    Approach: DP (Tabular, bottom-up)
    You don't need to store all dp array. by Maksim Shekhunov(WhatCanWeDo)
    
    T=O(mn) Beats 80 %, S=O(n) 98 %
    """
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        len_word1 = len(word1) if word1 else 0
        len_word2 = len(word2) if word2 else 0

        prev = list(range(len_word2+1))
        cur = [0] * (len_word2 + 1)

        for r in range(1, len_word1+1):
            cur[0] = r
            for c in range(1, len_word2+1):
                if word1[r-1] == word2[c-1]:
                    cur[c] = prev[c-1]
                else:
                    cur[c] = min(
                        prev[c],   # Insert
                        cur[c-1],  # Delete
                        prev[c-1]  # Replace
                    ) + 1

            prev = cur
            cur = [0] * (len_word2 + 1)

        return prev[-1]

    def minDistance_bak(self, word1: str, word2: str) -> int:
    """
    Approach: DP (Tabular, bottom-up) 
    by Tarun Nayak(N7_BLACKHAT)
    
         h  o  r  s  e
      0  1  2  3  4  5
    r 1  1  2  2  3  4
    o 2  2  1  2  3  4
    s 3  3  2  2  2  3

    T=O(mn) Beats 52.95 %, S=O(mn)14 %
    """
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        len_word1 = len(word1) if word1 else 0
        len_word2 = len(word2) if word2 else 0

        # word1: row, word2: col
        cost = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]

        # first column: The cost of change without word2
        for r in range(1, len_word1+1):
            cost[r][0] = r

        # first row: The cost of change without word1
        for c in range(1, len_word2+1):
            cost[0][c] = c

        for r in range(1, len_word1+1):
            for c in range(1, len_word2+1):
                if word1[r-1] == word2[c-1]:
                    cost[r][c] = cost[r-1][c-1]
                else:
                    cost[r][c] = min(
                        cost[r-1][c],   # Insert
                        cost[r][c-1],   # Delete
                        cost[r-1][c-1]  # Replace
                    ) + 1

        return cost[len_word1][len_word2]


# I referenced and modified the code from a Leetcode user Tarun Nayak(N7_BLACKHAT) and Maksim Shekhunov(WhatCanWeDo)


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
         h  o  r  s  e
      0  1  2  3  4  5
    r 1  1  2  2  3  4
    o 2  2  1  2  3  4
    s 3  3  2  2  2  3

    T=O(n**2), S=O(n**2)
    """
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            return 0

        m = len(word1)
        n = len(word2)

        cost =[[0] * (n + 1) for _ in range(m + 1)]

        # Left column: The cost of change when word2 is empty
        for i in range(1, m+1):
            cost[i][0] = i

        # Top line: The cost of change when word1 is empty
        for j in range(1, n+1):
            cost[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    cost[i][j] = cost[i-1][j-1]
                else:
                    cost[i][j] = min(
                        cost[i-1][j-1], 
                        cost[i-1][j],
                        cost[i][j-1]
                    ) + 1

        return cost[m][n]

    # referenced and modified the example code from N7_BLACKHAT

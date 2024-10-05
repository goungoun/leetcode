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
        if not word1 and not word2:
            return 0
        elif not word1 and word2:
            return len(word2)
        elif not word2 and word1:
            return len(word1)

        len_word1 = len(word1)
        len_word2 = len(word2)

        # word1: row, word2: col
        cost = [[0] * (len_word2 + 1) for _ in range(len_word1 + 1)]

        # Left column: The cost of change when word2 is empty
        for row in range(1, len_word1+1):
            cost[row][0] = row

        # Top line: The cost of change when word1 is empty
        for col in range(1, len_word2+1):
            cost[0][col] = col

        for row in range(1, len_word1+1):
            for col in range(1, len_word2+1):
                if word1[row-1] == word2[col-1]:
                    cost[row][col] = cost[row-1][col-1]
                else:
                    cost[row][col] = min(
                        cost[row-1][col-1], 
                        cost[row-1][col],
                        cost[row][col-1]
                    ) + 1

        return cost[len_word1][len_word2]

    # referenced and modified the example code from a Leetcode user N7_BLACKHAT

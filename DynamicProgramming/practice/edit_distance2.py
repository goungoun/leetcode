# 72. Edit Distance (Medium)
# https://leetcode.com/problems/edit-distance

import numpy as np

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        len_word1 = len(word1) if word1 else 0
        len_word2 = len(word2) if word2 else 0
        
        cost = [ [0]*(len_word2+1) for _ in range(len_word1+1) ]

        # initialize
        for col in range(1, len_word2+1):
            cost[0][col] = col

        for row in range(1, len_word1+1):
            cost[row][0] = row   
            for col in range(1, len_word2+1):
                if word1[row-1] == word2[col-1]:
                    cost[row][col] = cost[row-1][col-1]
                else:
                    ### Fix Here: the logic used to populate the matrix does not correctly implement the classic edit distance algorithm
                    cost[row][col] = max(
                        cost[row-1][col],
                        cost[row][col-1]) + 1

        print(np.array(cost))

        return cost[-1][-1]

# 72. Edit Distance (Medium)
# https://leetcode.com/problems/edit-distance

# Warning!! This code is to log my bug. It will return wrong result
# How to debug:
# print out the table
# add a couple of simple test cases e.g. word1 ="i", word2 ="i"

# import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return False

        len_col = len(word1)+1 if word1 else 1
        len_row = len(word2)+1 if word2 else 1

        cost = [ [0]*len_col for _ in range(len_row) ]

        for c in range(len_col):
            cost[0][c] = c

        for r in range(len_row):
            cost[r][0] = r

        # print(np.array(cost))

        for r in range(1,len_row):
            for c in range(1,len_col):
                # print(f"word1[c-1]={word1[c-1]}, word2[r-1]={word2[r-1]}")
                if word1[c-1] != word2[r-1]: # Fix: word1[c-1] == word2[r-1]
                    cost[r][c] = cost[r-1][c-1]
                else:
                    cost[r][c] =  min(
                        cost[r-1][c],
                        cost[r][c-1],
                        cost[r-1][c-1]
                    ) + 1
        
        # print(np.array(cost))
        return cost[-1][-1]

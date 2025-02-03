# 72. Edit Distance (Medium)
# https://leetcode.com/problems/edit-distance

#import numpy as np 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Measure minimum edit distance between two word
        return num_operations
    
        * operations
        I: Insert, U: Update, D: Delete, 
    
        Example 1: word1 is empty
        word1 = "", word2 = "ros"
        Insert r
        Insert o
        Insert s
        
            r o s
          0 1 2 3  ""-> ros : 3 operaions
    
        return 3
        
        Example 2: word1 and word2 are not empty
        word1 = "horse", word2 = "ros"
    
        Update h->r: rorse
        Delete r: rose
        Delete e: ros
    
            r o s
          0 1 2 3
        h 1 1 2 3  h-> ros : 3 oprations
        o 2 2 1 2  ho -> ros : 2 operations
        r 3 2 2 2  hor -> ros : 2 operations
        s 4 3 3 2  hors -> ros : 2 operations
        e 5 4 4 3  horse -> ros : 3 operations
    
        return 3
    
        Approach: Tabular, Bottom up DP
        Start from the smaller problem and record the result by filling a table
        Compare two characters in each position, reuse previously calculated result
        (if same +0, different +1)
        Repeat the same process until it gets the final distance, at the end of the cell
    
        T=O(mn) Beats 52.95 %, S=O(mn)14 %
        """
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
                  
        # print(np.array(cost))
        return cost[-1][-1]

# See also: edit_distance_optimized.py to improve space complexity. Replace cost[r] to cur and cost[r-1] to prev.

        

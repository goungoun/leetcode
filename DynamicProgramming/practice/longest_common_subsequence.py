# 1143. Longest Common Subsequence (Medium)
# https://leetcode.com/problems/longest-common-subsequence/

# Debug the solution and provide the fix

class Solution:
    def longestCommonSubsequence_full(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        l1 = len(text1) if text1 else 0
        l2 = len(text2) if text2 else 0 
        
        max_length = [[0]*l2 for _ in range(l1)]

        for r in range(1, l1):
            for c in range(1, l2):
                if text1[r+1] == text2[c+1]:
                    max_length[r][c] = 1 + max_length[r-1][c-1]
                else:
                    max_length[r][c] = max(
                        max_length[r-1][c], 
                        max_length[r][c-1]  
                        )

        return max_length[-1][-1]

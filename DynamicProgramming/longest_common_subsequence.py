# 1143. Longest Common Subsequence (Medium)
# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Longest Common Subsequence
        No change relative order, not necessarily consecutive

        return max_subsequence_length

        Example:
        Text1 = "abcde"
        Text2 = "ace"

        return 3

        Approach: Bottom up, Tabular
        
        T=O(mn), beats 93.88 %
        S=O(n), beats 91.28 %
        """
        if not text1 or not text2:
            return 0

        l1 = len(text1)+1 if text1 else 0
        l2 = len(text2)+1 if text2 else 0 
        
        curr = [0]*l2
        prv = [0]*l2

        for r in range(1, l1):
            for c in range(1, l2):
                if text1[r-1] == text2[c-1]:
                    curr[c] = 1 + prv[c-1]
                else:
                    curr[c] = max(
                        prv[c],
                        curr[c-1]
                        )
            prv = curr.copy()

        return prv[-1]
        
    def longestCommonSubsequence_full(self, text1: str, text2: str) -> int:
        """
        Approach: Bottom up, Full Tabular
        Make a table using Text1 as a row, Text2 as a column
        The first row is without any char from Text 1
        The first col is without any char from Text 2
        Increase the row index and col index, compare a single char from Text1 and Text2 in each index
        If chars are the same, increase one. If not, get the previous max subsequence.
        
            a c e 
          0 0 0 0
        a 0 1 1 1
        b 0 1 1 1
        c 0 1 2 2
        d 0 1 2 2
        e 0 1 2 3

        T=O(mn) beats 79.45%, 
        S=O(mn) beats 52.78%
        """
        if not text1 or not text2:
            return 0

        l1 = len(text1)+1 if text1 else 0
        l2 = len(text2)+1 if text2 else 0 
        
        max_length = [[0]*l2 for _ in range(l1)]

        for r in range(1, l1):
            for c in range(1, l2):
                if text1[r-1] == text2[c-1]:
                    max_length[r][c] = 1 + max_length[r-1][c-1]
                else:
                    max_length[r][c] = max(
                        max_length[r-1][c], # Insert
                        max_length[r][c-1]  # Delete
                        )

        return max_length[-1][-1]
        

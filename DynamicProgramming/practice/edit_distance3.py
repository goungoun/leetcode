# 72. Edit Distance
# https://leetcode.com/problems/edit-distance

# Warning!! This code is to log my bug. It will return wrong result

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0

        row_length = len(word1)+1 if word1 else 1
        col_length = len(word2)+1 if word2 else 1

        # initialize with all 0
        prev = list(range(col_length))
        curr = [0] * col_length

        for r in range(1,row_length):
            curr[0] = r
            for c in range(1,col_length):
                if word1[r-1] == word2[c-1]:
                    curr[c] = prev[c-1]
                else:
                    curr[c] = min(
                            prev[c],
                            curr[c-1],
                            prev[c-1]
                        ) + 1
            prev = curr

            # missing curr re-initialization causes wrong result
            # curr = [0] * col_length  # uncomment this to fix this

        return prev[-1]

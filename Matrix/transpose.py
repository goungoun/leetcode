# 867. Transpose Matrix
# https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, A):
        if not A:
            return []
            
        len_row = len(A) if A else 0
        len_col = len(A[0]) if A[0] else 0

        T = [[0]*len_row for _ in range(len_col)]

        for row in range(len_row):
            for col in range(len_col):
                T[col][row] = A[row][col]

        return T

  """
    def transpose_np(self, A):
        import numpy as np
        return np.transpose(np.array(A)).tolist()
  """

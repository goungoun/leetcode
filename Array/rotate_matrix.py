# 48. Rotate Image (Medium)
# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Roate an image in-place
        Do not return anything, modify matrix in-place instead.
        
        Example 1:
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        1,2,3
        4,5,6
        7,8,9

        7,4,1
        8,5,2
        9,6,3

        return [[7,4,1],[8,5,2],[9,6,3]]

        Example 2:
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        return [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i] = matrix[i][::-1]
        
        return matrix

    def rotate_bak(self, matrix: List[List[int]]) -> None:
        r = list(reversed(matrix))
        z = list(zip(*r))

        for i, l in enumerate(z):
            for j, val in enumerate(l):
                matrix[i][j] = val
       

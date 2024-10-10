# 48. Rotate Image (Medium)
# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Roate an image in-place
        Do not return anything, modify matrix in-place instead.

        Example:
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        [[7,4,1],[8,5,2],[9,6,3]]

        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        
        Approach:
        This is the original matrix
        1 2 3
        4 5 6
        7 8 9
        Swap matrix[i][j] and matrix[j][i] along the diagonal line
        1 4 7
        2 5 8
        3 6 9
        Reverse each line
        7 4 1
        9 5 2
        9 6 3
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                if i != j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            matrix[i] = matrix[i][::-1]
        
        return matrix

    # My first attempt beats only 13% in runetime, not good
    def rotate_deprecated(self, matrix: List[List[int]]) -> None:
        """
        Roate an image in-place
        Do not return anything, modify matrix in-place instead.

        Approach:
        This is the original matrix
        [[1 2 3]
         [4 5 6]
         [7 8 9]]
        First, reverse the order of rows
        [[7 8 9],
         [4 5 6],
         [1 2 3]]
        Zip it with the same column index
        (7,4,1)
        (8,5,2)
        (9,6,3)
        Use map(list, zipped) to convert tuples to lists
        """
        r = list(reversed(matrix))
        z = list(zip(*r))

        for i, l in enumerate(z):
            for j, val in enumerate(l):
                matrix[i][j] = val

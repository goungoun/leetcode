# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        Return Pascal's triange as a multi-dimensional array
        return p (pTriangle)

        Example:
        numRows = 5
        return [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
        [1]
        [1,1]
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]

        p[0][0] row = 0, col = 0
        p[1][0] p[1][1] row =1, col = 0~1
        p[2][0] p[2][1] p[2][2] row = 2, col = 0~2

        Approach:
        Use double for loop for the rows and columns
        1) Edges - just set 1 is ok
        2) None Edges - use the result of the previous row 
           p[row][col] = p[row-1][col-1] + p[row-1][col]

        Beats 99.40%
        """
        if not numRows:
            return []
            
        p = [[1]*(row+1) for row in range(numRows)]
  
        for row in range(2, numRows):
            for col in range(1, row):
                p[row][col] = p[row-1][col-1] + p[row-1][col]

        return p

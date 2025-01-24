# 2133. Check if Every Row and Column Contains All Numbers
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/description/

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        """
        Check the given matrix is valid
        return True/False

        Example 1: valid
        matrix = [
            [1,2,3],
            [3,1,2],
            [2,3,1]]

        Example 2: not valid
        matrix = [
            [1,1,1],
            [1,2,3],
            [1,2,3]]

        Approach:
        Use set to compare expected output and its row or column
        >>> set([1,2,3]) == set([3,2,1]) 
        True
        """
        if not matrix or len(matrix) == 0:
            return False

        n = len(matrix)

        # every row and column contains all the integers from 1 to n (inclusive)
        expected = {i for i in range(1, n+1)}
        
        for i in range(n):
            row = set()
            col = set()
            for j in range(n):
                row.add(matrix[i][j])
                col.add(matrix[j][i])

            if row != expected or col != expected:
                return False

        return True

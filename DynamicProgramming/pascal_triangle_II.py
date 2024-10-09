# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii  

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Generate pascal's triangle with O(rowIndex) extra space
        return p_row

        Example:
        rowIndex = 3
        
        [1,1,1,1]
        [1,1,1,1]
        [1,2,1,1]
        [1,3,3,1]
        
        return [1,3,3,1]

        Approach: Backward iteration
        Initialize p row with all 1
        Iterates backwards from i - 1 to 1 updating the value using previous row
        In this way, we can updatge the current value having next column of the row untouched

        Beats 85.95 %
        """
        if rowIndex is None:
            return []

        p = [1] * (rowIndex + 1)
        
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                p[j] = p[j] + p[j - 1]
        
        return p

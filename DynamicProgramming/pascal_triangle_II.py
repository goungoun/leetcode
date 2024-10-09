# 119. Pascal's Triangle II
# https://leetcode.com/problems/pascals-triangle-ii  

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        Last row of pascal's triangle 
        return row

        * F/U: O(rowIndex) extra space

        Example:
        rowIndex = 3

        1
        1 1
        1 2 1
        1 3 3 1
        
        [1,1,1,1]
        [1,1,1,1]
        [1,2,1,1]
        [1,3,3,1]
        
        return [1,3,3,1]

        Approach: Backward iteration
        Initialize p row with all 1
        Iterates backwards from i - 1 to 1 updating the value using the previous row
        In this way, we can update the current value having the next column of the row untouched

        Beats 89.25 %
        """
        if rowIndex is None:
            return []

        row = [1] * (rowIndex + 1)
        
        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        
        return row

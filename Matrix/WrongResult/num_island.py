# 200. Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of islands (4-directional connected components)
        return cnt_islands

        Example:
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]

        return 1

        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]

        return 3

        Approach: Count & Invert
        Within a double for-loop check the value "1" increases the count
        Set all adj elements and itself to "0" recursively to prevent double count

        Wrong Result!!! Fix This!!!
        """

        m = len(grid)
        n = len(grid[0])
        cnt_islands = 0

        def invertAdj(row, col):
            if row > m-1 or row < 0 or \
                col > n-1 or col < 0 or \
                grid[row][col] != "1":
                return

            grid[row][col] = "0"

            invertAdj(row, col-1) # left
            invertAdj(row, col+1) # right
            invertAdj(row-1, col) # up
            invertAdj(row+1, col) # down

        # O(mn)
        for row in range(m):
            for col in range(n):
                cnt_islands += 1
                invertAdj(row, col)

        return cnt_islands

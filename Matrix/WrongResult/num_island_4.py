# 200. Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands

# Warning!! This is a buggy code, need to fix
# Symptom : It returns the land count, not the island count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of island
        return cnt_islands

        * land: '1', water: '0' or empty, island: a group of lands surrounded by water

        Example 1: 9 lands -> 1 island
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]

        return 1

        Example 2: 7 lands -> 3 island
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]

        return 3

        Approach: DFS (or BFS is good too)
        First, implement a simple land count. This is just a nested for loop.
        Expand the idea to island by using recursive calls to remove duplicated counts
        Convert it to use stack to prevent stack overflow, the number of rows and columns will be up to 300, the maximum number of calls can be 90,000
        """
        if not grid or not grid[0]:
            return 0

        cnt_islands = 0
        m = len(grid)
        n = len(grid[0])

        LAND = "1"
        WATER = "0"

        def remove_duplicate(row, col):
            """
            Make LAND to WATER including the position and its adjacents
            """
            # Base condition
            if row < 0  or row >= m or \
                col < 0 or col >= n or \
                grid[row][col] != "LAND":  # Problem Here! LAND is a variabe, not a string
                return

            grid[row][col] = WATER

            # 4-directional adjacent
            remove_duplicate(row-1, col) # horizontal
            remove_duplicate(row+1, col) # horizontal
            remove_duplicate(row, col-1) # verticall
            remove_duplicate(row, col+1) # verticall

        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND:
                    cnt_islands += 1
                    remove_duplicate(r,c)

        return cnt_islands
      

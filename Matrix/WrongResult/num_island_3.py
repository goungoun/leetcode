# 200. Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands

# Warning!! This is a buggy code, need to fix
# Symptom : It returns the land count, not the island count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        LAND = "1"
        WATER = "0"

        m = len(grid) # m == grid.length
        n = len(grid[0]) # n == grid[i].length

        def dfs(row, col):
            if row < 0 or row >= m or \
                col < 0 or col >= n or grid[r][c] != LAND: # Problem Here: mixed variable use
                return

            #print(f"row={row}, col={col}, grid[r][c] ={grid[r][c]}")
            #print(f"row={row}, col={col}, grid[row][col] ={grid[row][col]}")
            grid[row][col] = WATER

            # adjacents
            dfs(row-1, col) # horizontal
            dfs(row+1, col) # horizontal
            dfs(row, col-1) # vertical
            dfs(row, col+1) # vertically

        
        cnt_island = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == LAND:
                    cnt_island += 1
                    dfs(r, c) # adjs won't be counted as an island
        
        print(f"grid={grid}")
        return cnt_island



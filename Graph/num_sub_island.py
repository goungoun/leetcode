# 1905. Count Sub Islands (Medium)
# https://leetcode.com/problems/count-sub-islands

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        """
        An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

        return cnt_sub_island

        Example:
        grid1 = [
            [1,1,1,0,0],
            [0,1,1,1,1],
            [0,0,0,0,0],
            [1,0,0,0,0],
            [1,1,0,1,1]]
        grid2 = [
            [1,1,1,0,0],
            [0,0,1,1,1],
            [0,1,0,0,0],
            [1,0,1,1,0],
            [0,1,0,1,0]
        ]
        
        islands=[
            [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4)], 
            [(2, 1)], 
            [(3, 0)], 
            [(3, 2), (3, 3), (4, 3)], 
            [(4, 1)]]

        sub_islands=[
            [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (1, 4)], 
            [(3, 0)], 
            [(4, 1)]]

        return 3

        Approach:
        Make a list of islands from the grid2
        Iterate the list of island and check the same position from the grid1
        If the value is 1, it is a sub island
        """
      
        islands = []
        grid = copy.deepcopy(grid2) # must use deep copy for 2D array
        m = len(grid)
        n = len(grid[0])
        
        def makeIsland(row, col):
            if row >= m or col >= n or row < 0 or col < 0 or grid[row][col] != 1:
                return

            tmp.append((row, col))
            grid[row][col] = 0

             # 4 directional
            makeIsland(row-1, col)
            makeIsland(row+1, col)
            makeIsland(row, col-1)
            makeIsland(row, col+1)

            return

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    tmp = []
                    makeIsland(row, col)
                    islands.append(tmp.copy())

        cnt_sub_island = 0
        
        # Validate sub island if the value from the grid1 is the same
        for island in islands:
            is_sub = True
            for row,col in island:
                if grid1[row][col] != 1:
                    is_sub = False
                    break
            if is_sub == True:
                cnt_sub_island += 1

        return cnt_sub_island

        
         

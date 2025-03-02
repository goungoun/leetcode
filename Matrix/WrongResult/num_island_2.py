# 200. Number of Islands (Medium)
https://leetcode.com/problems/number-of-islands

# Warning!! This is a buggy code, need to fix
# Symptom : It returns the land count, not the island count

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Count the number of island

        * land: "1", water: "0", island: all lands surrended by water (4-directionally)

        Example 1: one land
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]

        return 1

        Example 2: three lands
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
        
        return 3

        Appraoch: BFS
        Model the problem using recursive function
        Just count lands are not enough to handle adjacent land duplication
        To remove duplicated count, adjacent land will be convert to water

        If time allowed, recursive call should be (-> must be) converted to stack
        It is to prevent stack overflow, m, n can be up to 300, 300x300 = 90,000
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid) # m == grid.length
        n = len(grid[0]) # n == grid[i].length

        # Problem Here! Remove return and apply the right indentation
        def adj_to_water(row,col):
            """
            All lands surrounded by the water becomes water, including the one itself
            """
            # valid edge: 0<=row<m, 0<=col<n
            if 0<=row<m and 0<=col<n and grid[row][col] == "1":
                #print (f"grid[r][c]={grid[r][c]}")
                grid[row][col] = "0"
                return

            # 4-directional : vertical and horizontal
            adj_to_water(row-1,col)
            adj_to_water(row+1,col)
            adj_to_water(row,col-1)
            adj_to_water(row,col+1)

        island_cnt = 0

        for r in range(m):
            for c in range(n):      
                if grid[r][c] == "1": # 1: land
                    island_cnt += 1
                    adj_to_water(r,c)

        return island_cnt

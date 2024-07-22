# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Mesure the length of a island perimeter
        return perimeter

        Example:
        grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        [0,1,0,0]
        [1,1,1,0]
        [0,1,0,0]
        [1,1,0,0]

        4 edges x 7 lands = 28 edges
        6 * 2 adj edges
        28 - 12 = 16

        Approach:
        Extend the idea of a simple land count using a nested for loop
        One land is surrounded by the the 4 edges, so + 4
        If the edge is connected to the other adj lands, exclude them from the length
        """

        m = len(grid)
        n = len(grid[0])

        land_count = 0
        adj_edges = 0

        # O(mn)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    land_count += 1
                    
                    adj = [(row,col-1), (row,col+1), (row-1,col), (row+1,col)]
                    adj_land = [(r,c) for r,c in adj \
                                 if 0 <= r < m and 0 <= c < n and grid[r][c]==1]
                    adj_edges += len(adj_land)

        # A land consists of 4 edges
        perimeter = (land_count * 4) - adj_edges

        return perimeter

# 200. Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands

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
        Within a double for-loop check the value "1" increases the count.
        Set all adj elements and itself to "0" recursively to prevent double count.
        Use stack, queue or recursive call. In this case a list is used as a stack.
        """
      
        if grid is None:
            return None

        m = len(grid)
        n = len(grid[0])

        cnt_island = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    cnt_island += 1 
                    
                    # self + neighbors: "1" -> "0"
                    stk = [(row, col)]
                    visited = set((row, col))

                    while stk:
                        r, c = stk.pop()
                        grid[r][c] = "0"

                        for r,c in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                            if 0 <= r <m and 0 <= c < n and \
                                (r,c) not in visited and \
                                grid[r][c] == "1":
                                stk.append((r,c))
                                visited.add((r,c))

        return cnt_island

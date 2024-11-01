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
        Within a double for-loop check the value "1" increases the count
        Set all adj elements and itself to "0" using BFS to prevent double count
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        cnt_islands = 0

        # O(mn)
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    cnt_islands += 1
                    q = deque(((row, col),))
                    visited = set(((row, col),))
        
                    while q:
                        r,c = q.popleft() # bfs:popleft(), dfs:pop()
                        grid[r][c] = "0"
                        adjs = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
                        
                        for r, c in adjs:                   
                            if 0 <= r < m and 0 <= c < n and (r,c) not in visited and grid[r][c] == "1":
                                visited.add((r,c))
                                q.append((r,c))

        return cnt_islands
      

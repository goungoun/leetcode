# 994. Rotting Oranges (Medium)
# https://leetcode.com/problems/rotting-oranges

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Estimate the time of rotten oranges spread to all fresh oranges.
        The 4-directional adjacents become to a rotten orange every min.
        return mins or -1

        * 0: empty cell
        * 1: fresh orange
        * 2: rotten orange (*)

        Example: 
        2 1 1
        1 1 0
        0 1 1

        1 min:
        2 2 1
        2 1 0
        0 1 1

        2 mins:
        2 2 2
        2 2 0
        0 1 1

        3 mins:
        2 2 2
        2 2 0
        0 2 1

        4 mins:
        2 2 2
        2 2 0
        0 2 2

        return 4

        Approach: BFS

        2024.11.08 Removed visited to save space and updated grid[r][c]
        """
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        q = deque([])
        cnt_fresh_orange = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r,c))                    
                elif grid[r][c] == 1:
                    cnt_fresh_orange += 1

        if cnt_fresh_orange == 0:
            return 0

        mins = 0

        while q and cnt_fresh_orange > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                adjs = [
                    (r-1,c), # top
                    (r+1,c), # bottom
                    (r,c-1), # left
                    (r,c+1)  # right
                ]
                valid_adj = [(r,c) for (r,c) in adjs 
                    if 0<=r<m and 0<=c<n and grid[r][c] == 1]

                for r,c in valid_adj:
                    q.append((r,c))
                    grid[r][c] = 2
                    cnt_fresh_orange -= 1
                
            mins += 1
        
        return mins if cnt_fresh_orange == 0 else -1

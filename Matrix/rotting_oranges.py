# 994. Rotting Oranges (Medium)
# https://leetcode.com/problems/rotting-oranges

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Estimate the time of rotten oranges spread to adjacent fresh oranges.
        return mins

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
        """

        if not grid or not grid[0]:
            return -1

        m = len(grid)
        n = len(grid[0])

        cnt_fresh = 0

        FRESH = 1
        ROTTEN = 2

        q = deque([])
        visited = set()
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == FRESH: 
                    cnt_fresh += 1
                elif grid[row][col] == ROTTEN:
                    q.append((row,col))
                    visited.add((row, col))

        if cnt_fresh == 0:
            return 0

        mins = -1
        
        #import numpy as np
        while q:
            #print(np.array(grid))
            for _ in range(len(q)):
                row, col = q.popleft()
                
                if grid[row][col] == FRESH:
                    #grid[row][col] = ROTTEN
                    cnt_fresh -= 1

                adjs = [(row-1, col), 
                        (row+1, col), 
                        (row, col-1), 
                        (row, col+1)]

                adjs = [(row, col) for (row, col) in adjs \
                        if 0 <= row < m and 0 <= col < n \
                            and grid[row][col] != 0
                            and (row, col) not in visited]

                for adj in adjs:
                    q.append(adj)
                    visited.add(adj)

            mins += 1

        return mins if cnt_fresh == 0 else -1
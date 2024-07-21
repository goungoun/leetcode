# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/

from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Change the pixel color of an image including 4-directional adjacents
        return image

        Example 1: original_color <> color
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1, sc = 1
        [1,1,1] 
        [1,1,0] 
        [1,0,1]
        
        color = 2
        [2,2,2] 
        [2,2,0] 
        [2,0,1]

        return [[2,2,2],[2,2,0],[2,0,1]]

        Example 1: original_color == color
        image = [[0,0,0],[0,0,0]]
        sr = 0, sc = 0
        [0,0,0]
        [0,0,0]
        color = 0

        return [[0,0,0],[0,0,0]]

        Approach:
        First, change the color itself at the position (sr, sc)
        Change it only when the current color is different from the color
        Use BFS (or DFS) to fill other 4 adjacent colors: left, right, up and down
        """

        m = len(image)
        n = len(image[0])

        # BFS
        queue = deque([(sr,sc)])
        target_color = image[sr][sc]

        while queue:
            (row, col) = queue.popleft()
            curr_color = image[row][col]
            
            if curr_color == target_color and curr_color != color:
                image[row][col] = color

                adjs = [(row,col-1), 
                        (row,col+1), 
                        (row-1,col), 
                        (row+1,col)]

                valid_adjs = [(r, c) for r, c in adjs \
                    if r >= 0 and c >= 0 and r < m and c < n]

                for row,col in valid_adjs:
                    queue.append((row, col))

        return image

        
      

# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Change the color of a image by filling 4-direcional connected component
        return image

        sr, sc : starting point of the fill
        A color of the pixel is image[sr][sc]

        Approach: 
        recursively fill 
        from the current position as a center to the left, right, top, down
        For optimization, do not reapply the color if already has the target color
        
        Example:
        image = [[1,1,1],[1,1,0],[1,0,1]], 
        (sr, sc) = (1, 1), color change : 1 -> 2

        start: image[1][1]
        [2,2,2] 
        [2,2,0] 
        [2,0,1]

        return [[2,2,2], [2,2,0], [2,0,1]]
        """
        len_row = len(image)
        len_col = len(image[0])

        def flood(row, col, prv_color):
            if row > len_row - 1 or row < 0 or col > len_col - 1 or col < 0 or \
                image[row][col] == color or image[row][col] != prv_color:
                return
            
            image[row][col] = color

            flood(row, col-1, prv_color) # left
            flood(row, col+1, prv_color) # right
            flood(row-1, col, prv_color) # top
            flood(row+1, col, prv_color) # down

        flood(sr, sc, image[sr][sc])

        return image

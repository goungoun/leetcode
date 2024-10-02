# 130. Surrounded Regions (Medium)
# https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Find surrounding regions and update board, from "O" to "X"
        None of the region cells are on the edge of the board
        Do not return anything, modified board in-place instead.

        Example 1:
        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
            ]
        
        The bottom region is on the edge, not captured
        board = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
            ]        

        Approach:
        First, check all the edges using dfs to detect exit and temporarily mark them to "E"
        The remaining "O" cells can be captured surrounded with "X", so replace it with "X"
        Revert "E" back to the original value "O" 
        """
        m = len(board)
        n = len(board[0])

        def detectExit(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
                return

            board[row][col] = 'E'
            detectExit(row-1, col)
            detectExit(row+1, col)
            detectExit(row, col-1)
            detectExit(row, col+1)

        for col in range(n):
            detectExit(0, col)
            detectExit(m-1, col)

        for row in range(1, m-1):
            detectExit(row, 0)
            detectExit(row, n-1)
            
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "E":
                    board[row][col] = "O"

        

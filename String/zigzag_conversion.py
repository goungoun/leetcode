# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Read a string and convert it with a zigzag pattern

        Example:
        s = "PAY", numRows = 3
        P
        A
        Y

        return "PAY"

        s = "PAYPAL", numRows = 3
        P     A
        A  P  L
        Y

        return "PAAPLY"

        s = "PAYPALISHIRING", numRows = 3
        P   A   H   N
        A P L S I I G
        Y   I   R

        return "PAHNAPLSIIGYIR"

        Approach:
        Use True/False flag to decide its direction Up and Down
        Change the direction around the top (first row) and the bottom (last row)
        Used dictionary instead of 2-D array initialization as it will going be sparse
        """
        if s is None or len(s) <= 1 or numRows == 1:
            return s
        
        d = {} # key: (row,col), value: char
        is_down = True
        
        row, col = -1, 0
        max_row, max_col = 0, 0

        # T=O(n), S=O(n)
        for c in s:
            if is_down:
                row += 1
                max_row = max(row, max_row)
            else:
                row -= 1
                col += 1
                max_col = max(col, max_col)

            d[(row, col)] = c

            if row == numRows - 1:
                is_down = False
            elif row == 0:
                is_down = True

        ret = []
        for i in range(max_row+1):
            for j in range(max_col+1):
                if (i,j) in d:
                    ret.append(d[(i,j)])

        return "".join(ret)

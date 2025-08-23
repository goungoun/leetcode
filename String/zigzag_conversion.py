# 6. Zigzag Conversion (Medium)
# https://leetcode.com/problems/zigzag-conversion

class Solution:
    """
    Convert the given string s to a zigzag pattern
    return str_converted

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
    """
    def convert(self, s: str, numRows: int) -> str:
        if not s or not numRows:
            return 

        tmpSpace = [[] for _ in range(numRows)]

        is_down = True
        row = 0

        for token in s:
            tmpSpace[row].append(token)

            if row == numRows -1:
                is_down = False
            elif row == 0:
                is_down = True

            if is_down:
                row += 1
            else:
                row -= 1
                row = max(0, row)

        ret = []

        for r in tmpSpace:
            ret.append("".join(r))

        return "".join(ret)

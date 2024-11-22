# 22. Generate Parentheses (Medium)
# https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        For the each positions make a decision open or close
        return valid

        constraints:
        1 <= n <= 8
        """
        tmp = []
        ret = []
        len_full = n * 2

        self.left_count = 0
        self.right_count = 0

        def dfs():
            if len(tmp) == len_full:
                ret.append("".join(tmp))
                return

            if self.left_count < n:
                tmp.append("(")
                self.left_count += 1
                dfs()
                tmp.pop()
                self.left_count -= 1

            if self.right_count < self.left_count:
                tmp.append(")")
                self.right_count += 1
                dfs()
                tmp.pop()
                self.right_count -= 1

        dfs()
        
        return ret

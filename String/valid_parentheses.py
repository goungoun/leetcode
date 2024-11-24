# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Check if parentheses are valid
        return True (or False)

        Example 1: return True
        s = "()"
        s = "()[]{}"
        s = "([])"

        Example 2: return False
        s = "(]"

        Appraoch:
        Iterate characters in the string
        If it is an opener, put in the stack
        If it is a closer, check the top of the stack to see if it does d with the latest opener

        T=O(n)
        S=O(n)
        """
        if not s:
            return False

        stack = []

        # key: closer, value: opener
        d = {')':'(', 
                 '}':'{',
                 ']':'['}
        
        closers = d.keys()

        for token in s:
            if token in closers and not stack:
                return False
            elif token in closers:
                if stack.pop() != d[token]:
                    return False
            else:
                stack.append(token)

        # e.g '[' is not valid
        if stack:
            return False

        return True

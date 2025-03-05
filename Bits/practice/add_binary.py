# 67. Add Binary
# https://leetcode.com/problems/add-binary

from collections import deque 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a and not b:
            return ""
        elif not a:
            return b
        elif not b:
            return a
        
        i = len(a)-1
        j = len(b)-1

        carry = 0
        q = deque([])
 
        while i >= 0 or j >= 0:
            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0

            ?, ? = divmod(n1 + n2 + carry, 2) # Complete here: which one is the remainder
            q.?(r) # Complete here

            i -= 1
            j -= 1

        if carry > 0:
            q.?(carry) # Complete here

        return "".join(map(str,q))


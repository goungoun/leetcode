# 67. Add Binary
# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary numbers, a + b
        return sum

        Idea:
        Use Stack to access the number at the end of the string
        (Or it would be good to use two indexes for each number)

        Example:
        a = "11", b = "1"
          11
        +  1
        ----
         100

        a = "1010", b = "1011"
           1010
          +1011
          -----
          10101
        """

        l1 = [int(x) for x in a]
        l2 = [int(x) for x in b]

        carry = 0
        l = []

        while l1 or l2:
            n1 = l1.pop() if l1 else 0
            n2 = l2.pop() if l2 else 0

            carry, r = divmod(n1 + n2 + carry,2)
            l.append(str(r))

        if carry > 0:
            l.append(str(carry))

        return "".join(l[::-1])

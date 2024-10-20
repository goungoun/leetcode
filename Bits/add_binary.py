# 67. Add Binary
# https://leetcode.com/problems/add-binary

from collections import deque 

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Add two binary numbers, a + b
        return sum

        Intuition:
        I cannot use bin() to add binary
        > a = bin(11)
        > b = bin(11)
        a + b
        '0b10110b1011'

        Approach: type conversion
        When convert the value to the integer, let the function int() knows the string is binary numeral
        Directly add two integers
        Convert integer to binary and remove the prefix '0b'

        Example:
        a = "11", b = "1"
        > int("11",2) = 3
        > int("1",2) = 1
        > 3 + 1 = 4
        > bin(4) = '0b100'
        return "100"

        T=O(1), S=O(1)
        """
        if not isinstance(a,str) or not isinstance(b,str):
            return ""

        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary_bak1(self, a: str, b: str) -> str:
        """
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
          
        Approach: Use Stack
        Use Stack to access the number at the end of the string

        T=O(n), S=O(n)
        """
        if not a and not b:
            return ""

        l1 = [int(x) for x in a] if a else []
        l2 = [int(x) for x in b] if b else []

        carry = 0
        q = deque([])

        while l1 or l2:
            n1 = l1.pop() if l1 else 0
            n2 = l2.pop() if l2 else 0

            carry, r = divmod(n1 + n2 + carry,2)
            q.appendleft(r)

        if carry > 0:
            q.appendleft(carry)

        return "".join(map(str,q))

    def addBinary_bak2(self, a: str, b: str) -> str:
        """
        Approach: Index
        Start from the end of each string
        While decreasing indexs, add numbers and a carry

        T=O(n), S=O(n)
        """
        if not a and not b:
            return ""

        l1 = [int(x) for x in a] if a else []
        l2 = [int(x) for x in b] if b else []

        carry = 0
        q = deque([])
        i = len(l1)-1
        j = len(l2)-1

        while i >= 0 or j >= 0:
            n1 = l1[i] if i >= 0 else 0
            n2 = l2[j] if j >= 0 else 0

            carry, r = divmod(n1 + n2 + carry, 2)
            q.appendleft(r)

            i -= 1
            j -= 1

        if carry > 0:
            q.appendleft(carry)

        return "".join(map(str,q))

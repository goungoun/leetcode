# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check a given integer is a palindrome or not
        return True

        Approach:
        All negative integer is not palandrome
        Return True if a reversed string and the string is the same
        * reversed(s) will return iterable object, it should be converted to list and then back to string ex) "".join(list(reversed(s)))
        * Or string can be revered using s[::-1]

        Example:
        x = 121
        r = 121
        return True

        x = -121
        r = 121-
        return False

        x = 10
        r = 01
        return False
        """

        if x < 0:
            return False

        s = str(x)
        # rs = "".join(list(reversed(s)))

        return s == s[::-1]

# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Check it is a palindrome or not
        return True

        Example:
        x = 121
        return True

        x = -121
        return False

        x = 10
        return False
        """

        if x < 0:
            return False

        s = str(x)
        rs = "".join(list(reversed(s)))

        return s == rs

# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Check if s is a subsequence of t
        return True or False

        Approach:
        Two pointers for each string
        Move the pointer for s when the character exists while moving the other pointer for t
        If you can move the point at the end of the string s return True

        Example 1: Is a subsequence
        s = "abc"
        t = "ahbgdc"
        a,a : +1 
        b,h : -
        b,b : +1 
        c,g : -
        c,d : -
        c,c : +1 
        
        return True

        Example 2: Not a subsequence
        s = "axc"
        t = "ahbgdc"

        a,a: +1 
        x,h: -
        x,b: -
        x,g: -
        x,d: -
        x,c: -

        return False
        """
        if s is None or t is None:
            return False

        i, j = 0, 0
        len_s = len(s)
        len_t = len(t)

        # O(1) e.g. s = "abc", t="ab"
        if len_s > len_t:
            return False

        # O(n)
        while i < len_s and j < len_t:
            if s[i] == t[j]: 
                i += 1
                j += 1
            else:
                j += 1

        return i == len_s

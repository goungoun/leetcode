# 344. Reverse String
# https://leetcode.com/problems/reverse-string/description/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Reverse the string in the array s
        Do not return anything, modify s "in-place" instead.

        Approach:
        Use two pointer left(l) and right(r)
        Swap s[l], s[r] 
        Increase l and decrease r
        Repeat until l < r

        Example
        Input: s = ["h","e","l","l","o"]
        l=0,r=4 : s = ["o","e","l","l","h"]
        l=1,r=3 : s = ["o","l","l","e","h"]
        l=2,r=2 : <stop>

        Input: s = ["H","a","n","n","a","h"]
        s = ["h","a","n","n","a","H"] 
        if chars are the same, do not need to swap
        """

        l = 0
        r = len(s) -1

        while l < r:
            if s[l] != s[r]:
                s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
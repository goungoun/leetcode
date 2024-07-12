# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix
        return prefix

        Example:
        1) Found
        strs = ["flower","flow","flight"]
        return "fl"

        2) Not Found
        strs = ["dog","racecar","car"]
        return  ""

        Approach:
        Use zip to reconstruct strs
        And add character if the length of the set is zero
        (f,f,f) => len_set = 1 add f
        (l,l,l) => len_set = 1 add l
        (o,o,i) => len_set = 2 <stop>
        (w,w,g)
        """
        prefix = []
        z = zip(*strs)

        for t in z:
            s = set(t)
            if len(s) == 1:
                prefix.append(s.pop())
            else:
                break

        return "".join(prefix)
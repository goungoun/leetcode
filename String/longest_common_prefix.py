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
        And add character if the length of the set is 1
        (f,f,f) => len_set = 1 add f
        (l,l,l) => len_set = 1 add l
        (o,o,i) => len_set = 2 <stop>
        (w,w,g)

        T=O(mn)
        S=O(m + n)
        """
        if not strs:
            return ""
                    
        prefix = []
        z = zip(*strs)

        for t in z:
            s = set(t)
            if len(s) == 1:
                prefix.append(s.pop())
            else:
                break

        return "".join(prefix)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """
        Approach 2:
        Use array index without zip and set
        Check the length of the shortest string first, this is to limit the problem space
        For each string, check characters at the same position using nested loop

        T=O(mn)
        S=O(m)
        """
        if not strs:
            return ""

        len_strs = len(strs)
        min_len = float('inf')
        for s in strs:
            min_len = min(min_len, len(s))

        prefix = []
        for i in range(min_len):
            c = strs[0][i]
            for j in range(1, len_strs):
                if strs[j][i] != c:
                    return "".join(prefix)
            prefix.append(c)

        return "".join(prefix)

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        """
        Approach 3:
        Used the constraint range 0 <= strs[i].length <= 200, just start the loop without checking min length
        Reverted is_common flag False and break if not the same.

        T=O(mn)
        S=O(m)
        """
        if not strs:
            return ""
            
        prefix = ""
        first = ""
        curr = ""
        is_common = True

        for i in range(200):
            first = strs[0][i] if i < len(strs[0]) else ""
            for j in range(1,len(strs)):
                curr = strs[j][i] if i < len(strs[j]) else ""
                if first != curr:
                    is_common = False
                    break
            if is_common:
                prefix += first
            else:
                break

        return prefix

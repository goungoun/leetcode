# 3. Longest Substring Without Repeating Characters (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the longest contiguous substring without duplicated chars
        return max_length

        s = "abcabcbb"
        abc 3
        bca 3
        cab 3
        abc 3
        
        return 3

        s = "bbbbb"
        b 1
        
        return 1

        s = "pwwkew"
        pw 2
        wke 3
        kew 3

        return 3

        s = "tmmzuxt"
        tm 2
        mzuxt

        Approach: 
        use sliding window, use two pointers l and r
        i) increase r in one iteration 
        ii) if duplicate increase l until finding the duplicated char
        """

        l, r = 0, 0
        max_length = 0
        dup_chk = set()

        for r in range(len(s)):
            while s[r] in dup_chk:
                dup_chk.remove(s[l])
                l += 1
            dup_chk.add(s[r])
            max_length = max(max_length, (r-l)+ 1)
        
        return max_length

# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Looking for a way to figure out the first bad version minimizing the isBadVersion(n) API call
        return ver

        Example: n = 5, bad = 4
        isBadVersion(5) => True
        isBadVersion(4) => True
        isBadVersion(3) => False

        1 2 3 4 5 
        F F F T T

        mid = (1+5)//2 = 3 -> F (Go right)
        mid = (4+5)//2 = 4 -> T (Go left)
        mid = (4+4)//2 = 4 -> T

        return 4

        Approach:
        Decreasing its number by one would result too many API calls
        Apply binary search to decrease its search scope by half
        """
        ver = n
        l, r = 0, n

        while l <= r:
            mid = (l + r)//2
            is_bad = isBadVersion(mid)
            
            # if bad, go to left to find the first one
            if is_bad:
                ver = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ver

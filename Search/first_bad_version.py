# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Looking for a fast way to detect the first bad version minimizing a number of API calls
        return bad_version

        Example: n = 5, bad = 4
        isBadVersion(5) => True
        isBadVersion(4) => True
        isBadVersion(3) => False

        1 2 3 4 5 
        F F F T T
        ----> <--
        
        mid = (1+5)//2 = 3 -> F (Go right)
        mid = (4+5)//2 = 4 -> T (Go left)
        mid = (4+4)//2 = 4 -> T

        return 4

        Approach: Binary Search with two pointers
        Decreasing its number by one would result too many API calls
        Apply binary search to decrease its search space by half

        T=O(log n), s=O(1)
        """
        if n is None or n <= 0:
            return -1
            
        # last version by default, but this is not the first version
        bad_version = n

        # search space: 1 ~ n
        l, r = 1, n

        while l <= r:
            mid = (l + r)//2
            is_bad = isBadVersion(mid)
            
            # if bad, go to left to find the first one
            if is_bad:
                bad_version = mid
                r = mid - 1
            # if not, go to the right to find the bad one
            else:
                l = mid + 1
        
        return bad_version

# See also: binary_search.py

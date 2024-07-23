# 1051. Height Checker
# https://leetcode.com/problems/height-checker

from collections import Counter

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Check heights if it has the non-decreasing (=increasing) order
        return cnt_mismatch

        Example:
        heights  : [1,1,4,2,1,3]
        expected : [1,1,1,2,3,4]
        
        return 3

        Approach:
        The constraint of the hight, 1 <= heights[i] <= 100, is eligible for count sort
        This is about student's height, if initilized using array most of them will be sparse
        """
        counter = Counter(heights)
        
        expected = []
        for i in range(1,101):
            if i in counter:
                expected.extend([i]*counter[i])
        
        cnt_mismatch = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                cnt_mismatch += 1

        return cnt_mismatch

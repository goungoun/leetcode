# 1051. Height Checker
# https://leetcode.com/problems/height-checker/

# WARNING!! This code has many bugs, fix this by "dry run"!!

from typing import List

class Solution:
    def _bubbleSort(self, nums: List[int], n:int) -> List[int]:     
        for i in range(n):
            is_sorted = True
            for j in range(1,n-1-i):
                if nums[j] != nums[j-1]:
                    is_sorted = False
                    nums[j-1], nums[j] = nums[j], nums[j-1]
            if is_sorted:
                break 

        return nums

    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)
        
        #expected = sorted(heights)
        expected = self._bubbleSort(heights.copy(), n)

        print(f"heights={heights}, expected={expected}")

        return count(1 for i in range(n) if heights[i] != expected[i])

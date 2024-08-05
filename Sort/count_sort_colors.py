# 75. Sort Colors
# https://leetcode.com/problems/sort-colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort Colors in-place to make the same colors adjacent
        nums[i] is either 0(red), 1(white), or 2(blue)
        Do not return anything, modify nums in-place instead.
        
        a one-pass algorithm using only constant extra space 
        
        Approach:
        Count sort 
        """
        cnts = [0]*3
        for num in nums:
            cnts[num] += 1
        
        nums.clear()
        for i, cnt in enumerate(cnts):
            nums.extend([i]*cnt)

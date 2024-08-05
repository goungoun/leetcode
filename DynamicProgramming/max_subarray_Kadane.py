# 53. Maximum Subarray (Medium)
# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find a contiguous subarray that makes the largest sum
        return max_so_far

        Approach: Kadane's algorithm
        Iteratge each element, update max_ending_here 
        Update max_so_far as the maximum of either the current max_so_far or max_ending_here.
        If max_ending_here becomes negative, reset to zero 

        Example:
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        -2,1 => 1
        -2,1,-3 => -2 (reset)
        4 => 4
        4,-1,2,1 => 6
        4,-1,2,1,-5,4 => 5
        return 6

        Example:
        nums = [-2,-1,-3,-4]
        -2 => -2 (reset)
        -1 => -1 (reset)
        -3 => -3 (reset)
        -4 => -4 (reset)

        return -1
        """
        
        if nums is None or len(nums) == 0:
            return 
        max_ending_here, max_so_far = 0, float('-inf')

        for num in nums:
            max_ending_here += num
            max_so_far = max(max_so_far, max_ending_here)

            if max_ending_here < 0:
                max_ending_here = 0

        return max_so_far

# 53. Maximum Subarray (Medium)
# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Find a contiguous subarray that makes the largest sum
        return max_sum

        Example 1: negative values and positive values
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        -2,1 => 1
        -2,1,-3 => -2 (reset)
        4 => 4
        4,-1,2,1 => 6
        4,-1,2,1,-5,4 => 5
        return 6

        Example 2: All negative values
        nums = [-2,-1,-3,-4]
        -2 => -2 (reset)
        -1 => -1 (reset)
        -3 => -3 (reset)
        -4 => -4 (reset)

        return -1

        Example 3: Edge case, max_sum returns negative value (hidden)
        nums = [-1]
        -1 => -1 (reset)

        return -1

        Approach: Kadane's algorithm
        Iteratge each element, update curr_sum 
        Update max_sum as the maximum of either the current max_sum or curr_sum.
        If curr_sum becomes negative, reset to zero

        T=O(n), S=O(1)
        """
        if not nums:
            return 0

        curr_sum = 0
        max_sum = float('-inf')

        for num in nums:
            curr_sum += num
            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:              
                curr_sum = 0

        return max_sum


# Divide & Concour can improve the time and space complexity, O(log n)
# https://medium.com/@reza.shokrzad/exploring-kadanes-algorithm-a-path-to-maximum-subarray-ec1e8db6edab

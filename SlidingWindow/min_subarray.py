# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Find a subarray from the positive integers that the sum is more than a target
        return min_length

        Approach:
        Two Pointer l and r to the same direction
        Expand window by moving r to the right when the sum is less than target
        Shrink window by moving l to the right when the sum is larger than the target

        Example 1:
        nums = [2,3,1,2,4,3], target = 7
        l=0,r=0: 2 
        l=0,r=1: 2+3 = 5 
        l=0,r=2: 2+3+1 = 6 
        l=0,r=3: 2+3+1+2 = 8 > 7 => length=4
        l=1,r=3: 3+1+2 = 6 
        l=1,r=4: 3+1+2+4 = 10 > 7 => length=4
        l=2,r=4: 1+2+4 = 7 == 7 => length=3
        l=3,r=4: 2+4 = 6
        l=4,r=5: 2+4+3 = 9 > 7 => length=3
        l=5,r=5: 4+3 == 7 => length=2

        return 2

        Example (hidden): 
        nums=[12,28,83,4,25,26,25,2,25,25,25,12]

        return 8
        """
        # Not applicable sort because subarray is contiguous
        # nums.sort(reverse=True) 

        MAX_LENGTH = 100001

        min_length = MAX_LENGTH
        curr_length = 0
        curr_sum = 0
        l = 0

        # Expand window by increasing r
        for r in range(len(nums)):
            curr_sum += nums[r]

            # Shrink window by increasing l
            while curr_sum >= target:
                min_length = min(min_length, r-l+1)
                curr_sum -= nums[l]
                l += 1
                    
        return 0 if min_length == MAX_LENGTH else min_length

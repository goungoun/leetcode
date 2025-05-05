# 80. Remove Duplicates from Sorted Array II (Medium)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Update nums in-place, the sorted array, allowing two duplicate elements only
        return k (k: the length of the result)

        Example:
        nums = [1,1,1]
        nums = [1,1,_]
        return 2

        nums = [1,1,1,2,2,3]
        nums = [1,1,2,2,3,_]
        return 5

        nums = [0,0,1,1,1,1,2,3,3]
        nums = [0,0,1,1,2,3,3,_,_]
        return 7
        
        Approach:
        Use cnt for each value
        Compare previous value and the current value for each iteration of the given array nums 
        Reset the count if the value is not the same
        If cnt is less than 2, in-place update to the num and increase k

        T=O(n), S=O(1)
        """
        if not nums:
            return 0

        n = len(nums)
        cnt =  1
        k = 1

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                nums[k] = nums[i]
                k += 1

        return k



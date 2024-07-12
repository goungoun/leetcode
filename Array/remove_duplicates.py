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
        Use dup_cnt for each value
        Compare previous value and the current value for each iteration of the given array nums 
        Reset the count if the value is not the same
        If dup_cnt is less than 2, in-place update to the num and increase k
        """

        dup_cnt = 1
        k = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                dup_cnt += 1
            else:
                dup_cnt = 1

            if dup_cnt <= 2:
                nums[k] = nums[i]
                k += 1

        return k


        
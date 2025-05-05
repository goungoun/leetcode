# 2460. Apply Operations to an Array (Easy)
# https://leetcode.com/problems/apply-operations-to-an-array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:       
        n = len(nums)

        for i in range(0, n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0

        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in range(j, n):
            nums[i] = 0

        return nums

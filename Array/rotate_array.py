# 189. Rotate Array (Medium)
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the given integer array num k times
        + Try to come up with as many solutions as you can. (F/U)
        Do not return anything, modify nums in-place instead.

        Example 1:
        nums = [1,2,3,4,5,6,7], k = 3
        k = 1 [7,1,2,3,4,5,6]
        k = 2 [6,7,1,2,3,4,5]
        k = 3 [5,6,7,1,2,3,4]
        
        nums[-3:] == [5, 6, 7]
        nums[:-3] == [1, 2, 3, 4]

        Example 2:
        nums = [-1,-100,3,99], k = 2
        k = 1 [99,-1,-100,3]
        k = 2 [3,99,-1,-100]

        nums[-2:] == [3,99]
        nums[:-2] == [-1,-100]

        Example 3 (*):
        nums = [1,2,3], k = 5
        k = 1 [3,1,2]
        k = 2 [2,3,1] 
        k = 3 [1,2,3] <- Back to the initial list
        k = 4 [3,1,2] <- The same as k = 1
        k = 5 [2,3,1] <- The same as k = 2

        Approach:
        One approach can be using index slicing to perform several rotates at once

        """
        a = k % len(nums)
        nums[:] = nums[-a:] + nums[:-a]
        

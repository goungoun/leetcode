# 55. Jump Game (Medium)
# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Is it possible to reach the last index given the maximum jump?
        return True/False
        
        Example 1: Possible
        nums = [2,3,1,1,4]
        Start from the first index. Jump 1 step which is less than 2, and then 3 steps to the last index is ok
        return True

        Example 2: Not possible
        nums = [3,2,1,0,4]
        Always arrive at index 3, the value is 0 at the position. No jump further.
        return False

        Approach:
        Start from the last index the other way around
        Decrease the indexes and check to see if the given value is enough to reach the last index
        If enough it is ok to be just there in the remaining iterations. So change the target to the current position
        """
        last_idx = len(nums)-1

        for i in range(last_idx-1, -1, -1):
            if i + nums[i] >= last_idx:
                last_idx = i

        return last_idx == 0

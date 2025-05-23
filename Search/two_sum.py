# 1. Two Sum
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find out two numbers that the sum of them becomes the target
        return idxs # [idx1, idx2]

        * do not use the same element twice

        Example 1:
        nums = [2,7,11,15], target = 9
        nums[0] + nums[1] = 2 + 7 = 9
        return [0,1]

        Example 2:
        nums = [3,2,4], target = 6
        nums[1] + nums[2] = 2 + 4 = 6

        return [1,2]

        Example 3:
        nums = [3,3], target = 6
        nums[0] + nums[1] = 3 + 3 = 6

        return [0,1] # [0,0] or [1,1] cannot be the answer
        
        Approach:
        Buliding dictionary and search number within the same for loop. - well known approach!
        It is ok to pre-built dictionary such as d = {num:i for i, num in enumerate(nums)}
        But, have in mind that it keeps the last occurrence by overwriting when the number appears multiple times
        
        T=O(n), S=O(n)
        """
        if not nums:
            return []

        d = {}
        
        for i, num in enumerate(nums):
            search = target - num
            if search in d and i != d[search]:
                return [d[search], i]
            d[num] = i

        return []



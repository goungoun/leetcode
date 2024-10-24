# 1. Two Sum
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in nums such that they add up to target.
        return [i, j]

        Example:
        nums = [2,7,11,15], target = 9
        return [0,1]
        
        Approach:
        Buliding dictionary and search number within the same for loop. - well known approach!
        T=O(n), S=O(n)
        """
        d = {} # key=num, value=index

        for i, num in enumerate(nums):
            search = target - num
            if search in d:
                return [d[search], i]
            else:
                d[num] = i

    def twoSum_bak(self, nums: List[int], target: int) -> List[int]:
        """
        Approach: 
        This is easier approach to come up with easily from the beginning.
        Two phases, build dictionary and use. 
        T=O(n), S=O(n) - acceptable!
        """
        d = {num:i for i, num in enumerate(nums)} # key: nums, values: index

        for i, num in enumerate(nums):
            search = target - num
            if search in d and i != d[search]:
                return [d[search], i]



# 1. Two Sum
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Approach:
        Buliding dictionary and search number within the same for loop. T=O(n)
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
        This is easier approach to come up with easily from the beginning 
        You see, not a nested for loop it is also T = O(n) solution.
        """
        d = {} # key: nums, values: index
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            search = target - num
            if search in d and i != d[search]:
                return [d[search], i]


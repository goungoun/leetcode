# 1. Two Sum
# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        d = {} # key=num, value=index

        for i, num in enumerate(nums):
            search = target - num
            if search in d:
                return [d[search], i]
            else:
                d[num] = i

    def twoSum_bak(self, nums: List[int], target: int) -> List[int]:
        """
        This is easier approach to come up with easily, but for loop twice, less efficient than the one above.
        """
        d = {} # key: nums, values: index
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            search = target - num
            if search in d and i != d[search]:
                return [d[search], i]


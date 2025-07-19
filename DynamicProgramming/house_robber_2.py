# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/description/
class Solution:
    """
    Maximize the money you can get without visiting the adjacent house
    
    * Note: Houses are in a circle, first house is the neighbor of the last one

    return max_money

    Example 1:
    nums = [2,3,2]

    return 3

    Example 2:
    nums = [1]

    return 1

    Approach: Bottom up DP
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        def _rob(nums):
            pre, curr = 0, 0

            for num in nums:
                pre, curr = curr, max(curr, pre + num)

            return curr

        return max(_rob(nums[1:]), _rob(nums[:-1]))

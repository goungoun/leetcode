# 198. House Robber (Medium)
# https://leetcode.com/problems/house-robber

class Solution:
    """
    Maximize money without visiting adjacent houses
    return max_money

    * nums[i] = max(nums[i-2]+nums[i], nums[i-1])

    Approach: bottom up dp
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prv = 0
        pprv = 0

        for amount in nums:
            curr = max(pprv+amount, prv)
            pprv = prv
            prv = curr

        return prv

# 198. House Robber (Medium)
# https://leetcode.com/problems/house-robber

class Solution:
    """
    Maximize money without visiting adjacent houses
    return max_money

    * curr = max(pprv+amount, prv)

    Approach: bottom up dp
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        prv, curr = 0

        for amount in nums:
            prv, curr = curr, max(prv+amount, curr)

        return curr

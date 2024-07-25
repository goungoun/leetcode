# 136. Single Number
# https://leetcode.com/problems/single-number

from collections import Counter
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # leetcode deleted_user
        return reduce(lambda x, y: x ^ y, nums, 0)

    def singleNumber_neetcode(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = res ^ n
        return res

    def singleNumber_goun(self, nums: List[int]) -> int:
        c = Counter(nums)

        for key in c:
            if c[key] == 1:
                return key

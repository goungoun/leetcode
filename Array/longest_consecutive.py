# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Example:
        nums = [100, 4, 200, 1, 3, 2]
        """
        if not nums or len(nums)==0:
            return 0
        
        set_nums = set(nums)
        max_cnt = 1
        cnt = 1
        n = 0

        for num in nums:
            if num - 1 not in set_nums:
                cnt = 1
                n = 1
                while num + n in set_nums:
                    cnt += 1
                    n += 1
                max_cnt = max(cnt, max_cnt)   
        
        return max_cnt

# credit: niit
# TODO: union and find




        

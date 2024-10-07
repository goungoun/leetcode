# 128. Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        # Time Limit Exceeded!!!!
        Fix This..
        """
        if not nums:
            return 0

        # starters selection: if there is no such number less than the number, it is potentially a starters.
        set_nums = set(nums)

        starters = []
        for num in nums:
            if num - 1 not in set_nums:
                starters.append(num)

        # Given starterss, lets' check the longest subsequence... 
        max_cnt = 0
        for num in starters:
            cnt = 1
            while num + 1 in set_nums:
                cnt += 1
            max_cnt = max(max_cnt, cnt)

        return max_cnt






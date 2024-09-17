# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        return the length of the consecutive elements sequence

        Example:
        nums = [100, 4, 200, 1, 3, 2] * unsorted
        The longest consecutive sequence is [1,2,3,4]
        return 4

        Approach:
        Convert nums array list to a set
        Narrow down candidates eleigible for a starter of its consecutive sequence
        With that decreased scope, for each candidate, measure actual length of the sequence
        """
        if not nums or len(nums)==0:
            return 0

        set_nums = set(nums)
        starters = set([num for num in nums if num-1 not in set_nums])
        
        max_length = 1
        for starter in starters:
            length = 1       
            while starter + length in set_nums:
                length += 1
            max_length = max(length, max_length)

        return max_length
        



        

# 128. Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given unsorted nums, return the longest length of the consecutive elements sequence
        Write an algorithm O(n) runtime.
        return max_length

        Example 1:
        nums = [100, 4, 200, 1, 3, 2] * unsorted
        The longest consecutive sequence is [1,2,3,4]
        return 4

        Example 2: hidden case
        nums = [9,1,4,7,3,-1,0,5,8,-1,6] * unsorted, duplicated
        The longest consecutive sequence is [6,7,8,9]
        return 4

        Approach:
        Convert nums array list to a set
        Narrow down to a list of starters of its consecutive sequence
        For each starters, measure actual length of the sequence and get the max length
        """
        if not nums:
            return 0

        max_length = 1

        set_nums = set(nums)
        starters = set([num for num in nums if num-1 not in set_nums]) # handle duplicates ahead
        
        for starter in starters:
            length = 1       
            while starter + length in set_nums:
                length += 1
            max_length = max(length, max_length)

        return max_length
        

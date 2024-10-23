# 56. Merge Intervals (Medium)
# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals
        return merged_intervals

        Approach:
        Sort the list based on the first element, start
        If previous end is larger or equal than the current start, update the latest interval
        If not overlapped, add the interval
        """

        if not intervals:
            return []

        intervals.sort()
        
        ret = [[intervals[0][0], intervals[0][1]]]

        for start, end in intervals:
            if ret[-1][1] >= start:
                ret[-1][1] = max(end,ret[-1][1])
            else:
                ret.append([start, end])
                
        return ret

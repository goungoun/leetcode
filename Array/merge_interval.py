# 56. Merge Intervals (Medium)
# https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals
        return merged_intervals

        Example 1: Overlapped
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        return [[1,6],[8,10],[15,18]]

        Example 2: Not overlapped (hidden)
        intervals = [[1,4],[5,6]]
        return [[1,4],[5,6]]

        Approach:
        Sort the list based on the first element, start.
        If previous end is larger or equal than the current start, update the latest interval.
        If not overlapped, add the interval to the result.
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

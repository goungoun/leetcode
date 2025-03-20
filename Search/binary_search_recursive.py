# 704. Binary Search
# https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Write a binary search algorithm with O(log n) complexity
        nums are sorted in ascending order
        
        return index (not its value) if target exists, otherwise -1

        Approach: Divide & concour
        Pick an index in the middle if the value is the target return the index.
        If not, decrease the search scope by half and solve the smaller problem recursively.
        In that way, the time complexity becomes O(log n).
        """
        if not nums or target is None:
            return -1 
        
        def rec_search(l, r):
            if l > r:
                return -1

            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return rec_search(mid+1, r)                
            else:
                return rec_search(l, mid-1)
            
            return -1

        return rec_search(0, len(nums)-1)

# 704. Binary Search
# https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Write a binary search algorithm with O(log n) complexity
        nums are sorted in ascending order
        
        return index (not its value) if target exists, otherwise -1

        Approach: Divide & concour
        Replaced a recursive call to use stack
        """
        if not nums or target is None:
            return -1

        stk = [(0, len(nums) - 1)]

        while stk:
            l, r = stk.pop()
            if l > r:
                return -1

            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                stk.append((mid + 1, r))
            else:
                stk.append((l, mid - 1))
    
        return -1

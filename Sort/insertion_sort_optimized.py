# 1051. Height Checker
# https://leetcode.com/problems/height-checker

class Solution:
    def _insertionSort(self, arr):
        """
        Approach:
        Replaced the inner loop as a binary search to improve time complexity
        
        T=O(n*log n)
        S=O(1)
        """
        len_arr = len(arr)
        
        for i in range(1, len_arr):
            key = arr[i]

            # O(log n): 0 ~ i-1 is already sorted
            idx = self._binarySearch(arr, key, 0, i - 1)
            arr[idx + 1:i + 1] = arr[idx:i]
            arr[idx] = key

        return arr

    def _binarySearch(self, arr, key, left, right):
        """
        Binary Search
        It works only for sorted arr!

        T=O(log n)
        S=O(1)
        """
        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def heightChecker(self, heights: List[int]) -> int:
        """
        T=O(n*logn) beats 21.13%
        S=O(n) beats 15.18% 
        """
        if not heights:
            return 0
        
        n = len(heights)
        expected = self._insertionSort(heights.copy()) #in-place algorithm
        
        return sum(1 for i in range(n) if heights[i]!=expected[i])

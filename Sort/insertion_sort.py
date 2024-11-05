# 1051. Height Checker
# https://leetcode.com/problems/height-checker

class Solution:
    def insertionSort(self, arr):
        """
        T=O(n**2)
        S=O(1)
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr

    def heightChecker(self, heights: List[int]) -> int:
        """
        T=O(n**2) beats 5.38%
        S=O(n) beats 15.18% 
        """
        if not heights:
            return 0
        
        n = len(heights)
        expected = self.insertionSort(heights.copy()) #in-place algorithm

        return sum(1 for i in range(n) if heights[i]!=expected[i])

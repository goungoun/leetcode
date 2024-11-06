# 1051. Height Checker
# https://leetcode.com/problems/height-checker

class Solution:
    def _selectionSort(self, arr: List[int]) -> List[int]:
        """
        T=O(n**2)
        S=O(1)
        """
        n = len(arr)
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                        min_idx = j

            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def heightChecker(self, heights: List[int]) -> int:
        """
        Approach: Selection Sort
        Performed better than bubble sort due to less frequent element swap

        T=O(n**2), beats 20.46%
        S=O(n), beats 49.15%
        """
        if not heights:
            return 0
        
        n = len(heights)
        expected = self._selectionSort(heights.copy()) #in-place algorithm

        return sum(1 for i in range(n) if heights[i]!=expected[i])
      

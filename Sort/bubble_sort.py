# 1051. Height Checker
# https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Just to test bubble sort. 
        It passes leetcode test cases, but it performs the worst. 
        Please refer to count_sort.py for better solution.

        Only beats 5% at best
        """
        if not heights:
            return 0

        n = len(heights)
        is_sorted = False
        
        expected = heights.copy()

        # T=O(n**2), S=O(1)
        for i in range(n):
            is_sorted = True
            for j in range(n-i-1):
                if expected[j] > expected[j+1]:
                    expected[j], expected[j+1] = expected[j+1],expected[j]
                    is_sorted = False
            if is_sorted:
                break

        cnt_wrong_order = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                cnt_wrong_order += 1

        return cnt_wrong_order
        

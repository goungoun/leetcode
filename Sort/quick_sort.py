# 1051. Height Checker
# https://leetcode.com/problems/height-checker

class Solution:
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid_idx = len(arr)//2
        pivot = arr[mid_idx]

        left_arr = []
        mid_arr = []
        right_arr = []

        for num in arr:
            if num < pivot:
                left_arr.append(num)
            elif num > pivot:
                right_arr.append(num)
            else:
                mid_arr.append(num)

        return self.quick_sort(left_arr) + mid_arr + self.quick_sort(right_arr)

    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0

        n = len(heights)
        expected = self.quick_sort(heights)

        return sum(1 for x,y in zip(heights,expected) if x!=y)
        

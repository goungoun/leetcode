# 1051. Height Checker
# https://leetcode.com/problems/height-checker/

class Solution:
    def merge(self, arr1, arr2):
        idx1 = 0
        idx2 = 0
        len_arr1 = len(arr1)
        len_arr2 = len(arr2)

        # merge sort requires O(n) auxiliary space to hold the sorted elements
        ret = []

        while idx1 < len_arr1 and idx2 < len_arr2:
            val1 = arr1[idx1]
            val2 = arr2[idx2]
        
            if val1 < val2:
                ret.append(val1)
                idx1 += 1
            else:
                ret.append(val2) 
                idx2 += 1

        if idx1 >= 0:
            ret.extend(arr1[idx1:])
        if idx2 >= 0:
            ret.extend(arr2[idx2:])
        
        return ret
	
    def merge_sort(self, arr):
        """
        Divide and conquer resursive algorithm
        """
        # base condition
        if len(arr) == 1:
            return arr
        
        mid = len(arr)//2
        left = self.merge_sort(arr[mid:])
        right = self.merge_sort(arr[:mid])
        
        return self.merge(left, right)

    def heightChecker(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        n = len(heights)
        expected = self.merge_sort(heights)
        return sum(1 for i in range(n) if heights[i]!=expected[i])

# 912. Sort an Array
# https://leetcode.com/problems/sort-an-array

from heapq import heapify, heappop

class Solution:
    """
    Sort an array nums without built-in functions in O(nlog(n))
    return sorted_nums
    
    Example 1:
    nums = [5,2,3,1]
    return [1,2,3,5]

    Example 2:
    nums = [5,1,1,2,0,0]
    return [0,0,1,1,2,5]
    
    Approach:
    Need to specify the built-in function means sort() or sorted() 
    Quick Sort is easy to implement, but showed excedded memory for some cases 
    If heapify() is allowed just in case, it works as a in-place algorithm with less memory and passes all the cases
    """
  
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.heapSort(nums)
    
    def quickSort(self, nums: List[int]) -> List[int]:
        if nums is None or len(nums) <= 1:
            return nums
        
        mid = nums[len(nums)//2]

        l = []
        m = []
        r = []

        for num in nums:
            if num < mid:
                l.append(num)
            elif num > mid:
                r.append(num)
            else:
                m.append(num)

        return self.quickSort(l) + m + self.quickSort(r)
    
    def heapSort(self, nums: List[int]) -> List[int]:
        heapify(nums) # In-place
        ret = []

        for _ in range(len(nums)):
            num = heappop(nums)
            ret.append(num)

        return ret
        

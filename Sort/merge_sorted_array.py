# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge a sorted array nums2 into an another sorted array nums1
        Do not return anything, modify nums1 in-place instead.

        Example:
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
        return [1,2,2,3,5,6]
        """

        i = m-1
        j = n-1
        k = (m+n) - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        while j >= 0 and k >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        

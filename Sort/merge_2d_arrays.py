# 2570. Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values

class Solution:
    """
    Merge the two arrays into one array that is sorted in ascending order by id
    return result_array 
    """
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        if not nums1 and not nums2:
            return []
        elif not nums1:
            return nums2
        elif not nums2:
            return nums1

        i, j = 0, 0
        m, n = len(nums1), len(nums2)

        result_array = []

        while i < m and j < n:
            if nums1[i][0] < nums2[j][0]:
                elem = [nums1[i][0], nums1[i][1]]
                result_array.append(elem)
                i += 1
            elif nums1[i][0] > nums2[j][0]:
                elem = [nums2[j][0], nums2[j][1]]
                result_array.append(elem)
                j += 1
            else:
                elem = [nums1[i][0], nums1[i][1]+nums2[j][1]]
                result_array.append(elem)
                i += 1
                j += 1

        while i < m:
            elem = [nums1[i][0], nums1[i][1]]
            result_array.append(elem)
            i += 1

        while j < n:
            elem = [nums2[j][0], nums2[j][1]]
            result_array.append(elem)
            j += 1
        
        return result_array

        

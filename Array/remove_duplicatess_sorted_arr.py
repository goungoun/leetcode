# 26. Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates in-place from the sorted array 

        return k (k is the number of unique elements)

        Example 1: k = 2
        nums = [1,1,2]

        i=0: [1]
        i=1: compare(1,1) => [1]
        i=2: compare(1,2) => [1,2]

        return 2

        Approach: Two pointers
        One index i from the start to end
        The other j is to place the value
        Iterate the array nums and compare current value with the previous value

        T=O(n), S=O(1)
        """
        if not nums:
            return 0

        len_nums = len(nums)    
        j = 0

        for i in range(1, len_nums):
            if nums[i-1] != nums[i]:
                j += 1 # Increase j only when the current value is not the same with the previous one
                nums[j] = nums[i] # in-place update

        k = j + 1

        return k

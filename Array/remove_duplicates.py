# 80. Remove Duplicates from Sorted Array II (Medium)
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Update nums in-place, the sorted array, allowing two duplicate elements only
        return k (k: the length of the result)

        Example:
        nums = [1,1,1]
        nums = [1,1,_]
        return 2

        nums = [1,1,1,2,2,3]
        nums = [1,1,2,2,3,_]
        return 5

        nums = [0,0,1,1,1,1,2,3,3]
        nums = [0,0,1,1,2,3,3,_,_]
        return 7

        Approach: by niits
        The point is how we can decide whether current number is valid or not.
        Initialize k to 2 because the problem allows each unique element to appear at most twice.
        Compare the current value with the element located at k - 2.        

        T=O(n), S=O(1)
        Beats 81.45%
        """
        if not nums:
            return 0

        k = 2

        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1 

        return k
        
    def removeDuplicates_my(self, nums: List[int]) -> int:
        """
        Approach:
        Use cnt for each value
        Compare previous value and the current value for each iteration of the given array nums 
        Reset the count if the value is not the same
        If cnt is less than 2, in-place update to the num and increase k

        T=O(n), S=O(1)
        Beats 53.91%
        """

        if not nums:
            return 0

        cnt =  1
        k = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                nums[k] = nums[i]
                k += 1

        return k

# Referenced the solution by a leetcode user niits to compare my solution

# 189. Rotate Array (Medium)
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the given integer array num k times
        Do not return anything, modify nums in-place instead.

        F/U
        + Try to come up with as many solutions as you can. 
        + Could you do it in-place with O(1) extra space? ***

        Example: 
        nums = [1,2,3,4,5,6,7], k = 9
        group:  # # * * * * *, remainder r = 2
        
        return [6,7,1,2,3,4,5]
                
        Approach: Reverse
        Reverse all number.
        Reverse before r
        Reverse after r
        
        T=O(n), S=O(1)
        Beats 85.42%
        """
        if not nums:
            return []

        len_nums = len(nums)
        r = k % len_nums
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, len_nums - 1)
        reverse(0, r - 1)
        reverse(r, len_nums - 1)

        # See also: 344. Reverse String, 48. Rotate Image
        
    def rotate_idx1(self, nums: List[int], k: int) -> None:
        """
        Example 1:
        nums = [1,2,3,4,5,6,7], k = 3
        k = 1 [7,1,2,3,4,5,6]
        k = 2 [6,7,1,2,3,4,5]
        k = 3 [5,6,7,1,2,3,4]
        
        nums[-3:] == [5, 6, 7]
        nums[:-3] == [1, 2, 3, 4]

        Example 2:
        nums = [-1,-100,3,99], k = 2
        k = 1 [99,-1,-100,3]
        k = 2 [3,99,-1,-100]

        nums[-2:] == [3,99]
        nums[:-2] == [-1,-100]

        Example 3 (*):
        nums = [1,2,3], k = 5
        k = 1 [3,1,2]
        k = 2 [2,3,1] 
        k = 3 [1,2,3] <- Back to the initial list
        k = 4 [3,1,2] <- The same as k = 1
        k = 5 [2,3,1] <- The same as k = 2

        Approach:
        One approach can be using index slicing to perform several rotates at once
        Slicing requires auxiliary space, not a good idea
        
        T=O(n), S=O(n)
        """
        if not nums:
            return []
            
        r = k % len(nums)
        nums[:] = nums[-r:] + nums[:-r]
        
    def rotate_idx2(self, nums: List[int], k: int) -> None:
        """
        Approach:
        Slicing requires auxiliary space to copy elements, not a good idea

        T=O(n), S=O(n)
        """
        if not nums:
            return []
        
        r = k % len(nums)
        nums[:r], nums[r:] = nums[-r:], nums[:-r]

    def rotate_bad(self, nums: List[int], k: int) -> None:
        """
        Approach:
        This simulates rotating array exactly as explained.
        Bad idea, but if I have to suggest different algorithms.
        It would acceptable only when k is very small. 

        T=O(n^2), S=O(n)
        Beats 10.38%
        """
        if not nums:
            return []
            
        r = k % len(nums)
        
        # T=O(n*r), worst O(n^2)
        while r > 0:
            val = nums.pop() # O(1)
            nums.insert(0, val) # O(n), right shift values in nums to make a room for a new element
            r -= 1
        

# Referenced solutions from a leetcode user niits

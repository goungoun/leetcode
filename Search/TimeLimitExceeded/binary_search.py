# 704. Binary Search
# https://leetcode.com/problems/binary-search

# Time Limit Exceeded!!
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or not target: ## Fix This! target is None
            return False

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r - l)//2 ## Fix This! mid = l + (r - l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = nums[mid] + 1  ## Fix This! Hint: l and mid are index
            elif nums[mid] > target:
                r = nums[mid] - 1  ## Fix This! Hint: r and mid are index    

        return -1

        

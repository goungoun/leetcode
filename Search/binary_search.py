# 704. Binary Search
# https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Write a binary search algorithm with O(log n) complexity
        * nums are sorted in ascending order!
        
        return index (not its value) if target exists, otherwise -1
        
        Example: 
        nums = [-1,0,3,5,9,12], target = 9

        
        Index     0 1 2 3 4 5 
        pointer         ^   ^
        value    -1 0 3 5 9 12
        target        ?   !
        
        [-,-,-,-,9,12]
        l=0, r=5, mid=(0+5)//2=2 nums[mid]=3 < 9
        l=3, r=5, mid=(3+5)//2=4 nums[mid]=9 == 9
        return 9

        nums = [-1,0,3,5,9,12], target = 2
        [-1,0,3,5,9,12]
        l=0, r=5, mid=(0+5)//2=2 nums[mid]=3 > 2
        l=0, r=1, mid=(0+1)//2=0 nums[0]=-1 < 2
        l=1, r=1, mid=(1+1)//2=1 nums[1]=0 < 2
        l=2, r=1 <Stop>
        return -1

        nums = [5], target = 5
        return 5

        Appraoch: Two pointer
        Update left or right to decrease its search scope by half
        Take advantage of the fact that the elements in the array are sorted

        T=O(log n), S=O(1)
        """
        if not nums or target is None:
            return -1

        l = 0
        r = len(nums) -1 

        # l < r vs l <=r : to handle the case of having length 1, = is required
        while l <= r: # add equal because of its value can be the target
            mid = l + (r - l)//2 # to prevent overflow (l + r)//2, especially in other languages
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return -1

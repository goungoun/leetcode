# 215. Kth Largest Element in an Array (Medium)
# https://leetcode.com/problems/kth-largest-element-in-an-array

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Kth Largest Element in nums
        return num (not index)

        Idea:
        Use heap, but the python heap is meanheap by default
        So, *-1 to all elements in the nums and then return -smallest_value 

        Example:
        nums = [3,2,1,5,6,4], k = 2
        6,5 => return 5
        1) If max heap is supported, 
        nums = [3,2,1,5,6,4]
               6
            5    4
           2 3  1
        heappop() -> 6 : First Largest Element
              5
            3   4
           1 2  
        heappop() -> 5  : Second Largest Element

        2) for mean heap
        nums = [-3,-2,-1,-5,-6,-4]
               -6
            -5     -4
          -2  -3 -1
        heappop() -> -6 : First Smallest Element
                -5
            -3     -4
          -1  -2 
        heappop() -> -5 : Second Smallest Element

        return -(-5) : Second Largest Element, k=2
        """
        if not nums or not k or k <= 0:
            return None

        h = [-x for x in nums]
        heapify(h)

        for _ in range(k):
            smallest_val = heappop(h)

        return -smallest_val
        

    def findKthLargest_fu(self, nums: List[int], k: int) -> int:
        """
        Follow Up: Decrease the space complexity
        """
        if not nums or not k or k <= 0:
            return None
        
        h = [] 
        for num in nums:
            heappush(h, num) # min heap

            # Space requires only k, less than the length of nums
            if len(h) > k:
                heappop(h) 

        return h[0]

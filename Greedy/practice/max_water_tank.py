# 42. Trapping Rain Water (Hard)
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Trap maximum water with the height of each bar
        return water

        Approach:
        Two pointer
        Forward and Backward iteration

        T=O(n), S=O(1)

        ## Debug it!!
        Test case:
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        height = [1,0,0,0,0]
        """
        if not height:
            return 0

        len_height = len(height)
        water = 0

        l,r = 0, 0
        while r < len_height:
            if height[r] >= height[l]:
                for i in range(l, r):
                    water += height[l]-height[i]
                l = r
            r += 1

        l,r = len_height-1, len_height-1
        while l >= 0:
            if height[l] > height[r]:    
                for i in range(l, r):
                    water += height[r]-height[i]
                    r = l
            l -= 1

        return water
      

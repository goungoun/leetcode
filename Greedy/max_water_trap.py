# 42. Trapping Rain Water (Hard)
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Trap maximum water with the height of each bar
        return amt_water

        Approach:
        Two pointer
        Forward and Backward iteration
        Split into two parts using helper funcitons for easy debug      

        T=O(n), S=O(1)
        """
        if not height:
            return 0

        self.amt_water = 0
        last_idx = len(height) - 1    

        def forward():
            l, r = 0, 0
            while r <= last_idx:
                if height[l] < height[r]:
                    # calculate water
                    for i in range(l+1, r):
                        self.amt_water += max(height[l]-height[i], 0)
                    l = r
                r += 1
        
        def backward():
            l, r = last_idx, last_idx
            while l >= 0:
                if height[l] >= height[r]:
                    # calculate water
                    for i in range(l+1, r):
                        self.amt_water += max(height[r]-height[i], 0)
                    r = l
                l -= 1

        forward()
        backward()
        
        return self.amt_water 

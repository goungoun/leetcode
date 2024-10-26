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
        """
        if not height:
            return 0

        len_height = len(height)
        water = 0

        l,r = 0, 0
        while r < len_height:
            if height[r] >= height[l]:
                for i in range(l, r):
                    water += max(height[l]-height[i], 0)
                l = r
            r += 1

        l,r = len_height-1, len_height-1
        while l >= 0:
            if height[l] > height[r]:    
                for i in range(l, r):
                    water += max(height[r]-height[i], 0)
                r = l
            l -= 1

        return water
    
    def trap_bak(self, height: List[int]) -> int:
        """
        Approach:
        Two walls on the left and right works like a container
        Store the max height of the wall from the left and from the right
        Iterate each height and accumlate water, but adjust the elevated amount

        Example:
        height [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        max_l  [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
        max_r  [0, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
        water  [0, 0, 1, 0, 1, 2, 1, 0, 0, 1, 0, 0]

        sum of water = 1 + 1 + 2 + 1 + 1 = 6
        return 6

        T=O(n), S=O(n)
        """
        n = len(height)
        max_l = height.copy()
        max_r = height.copy()

        l = 1 # and l to the right
        while l < n:
            max_l[l] = max(max_l[l-1], height[l])
            l += 1

        r = n - 2 # and r to the left 
        while r > 0:
            max_r[r] = max(max_r[r+1], height[r])
            r -= 1

        # expected vs actual
        water = 0
        for i in range(n):
            expected = min(max_l[i], max_r[i])
            actual = max(0, expected - height[i]) # adj elevated height
            water += actual

        return water


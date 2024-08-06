# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Find two lines that maximize area of the water tank
        return max_area

        Example 1:
        height = [1,8,6,2,5,4,8,3,7]

        height[1] = 8
        height[8] = 7 
        
        width : 8 - 1 = 7, height = min(8,7) = 7
        area = width x height = 7 x 7 = 49

        return 49

        Example 2:
        height = [1,1]

        height[0] = 1
        height[1] = 1

        width : 1 - 0 = 1, height = min(1,1) = 1
        area = width x height = 1 x 1 = 1

        return 1

        Approach: Two pointers, Greedy
        Maximize the width first by setting two pointers at distance
        Take taller one while moving l to the right or r to the left
        Keep moving and update max area
        """

        max_area = 0

        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area

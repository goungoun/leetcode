# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water

class Solution:
    """
    Maximum amount of water of a container that is supported by two vertical straight lines
    return max_area

    Example 1:
    height = [1,8,6,2,5,4,8,3,7]

    l = 1: height[1] = 8
    r = 8: height[8] = 7

    width: = r - l = 7
    height = min(height[1], height[8]) = min(8, 7) = 7
    
    area = width x height = 7 x 7 = 49

    return 49

    Example 2:
    height = [1,1]

    l = 0: height[0] = 1
    r = 1: height[1] = 1

    width : 1 - 0 = 1, height = min(1,1) = 1
    area = width x height = 1 x 1 = 1

    return 1

    Approach: Two pointers, Greedy
    Maximize the width first by setting two pointers at distance
    Take taller one while moving l to the right or r to the left
    Keep moving and update max area
    """
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0

        max_area = 0
        n = len(height)

        l, r = 0, n - 1 # idx: 0 ~ n-1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            # discard the shorter bar and moving on
            if height[l] < height[r]:
                l += 1 # l to the right
            else:
                r -= 1 # r to the left

        return max_area
        

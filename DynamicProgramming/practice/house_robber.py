# 198. House Robber (Medium)
# https://leetcode.com/problems/house-robber/

# Warning!! 40 / 70 testcases passed!

class Solution:
    """
    Maximize the money by visiting houses except adjacent houses
    return max_money

    Example 1: 
    nums = [1,2,3,1]
    
    nums[0]=1, accumulated=1
    nums[2]=3, accumulated=4

    1 + 3 = 4

    nums[1]=2, accumulated=2
    nums[3]=1, accumulated=3

    1 + 2 = 3

    max(4,3) = 4

    return 4

    Example 2: nums = [2,7,9,3,1]
    idx 0 2 4: 2 + 9 + 1 = 12
    idx 1 3: 1 + 3 = 4

    max(4, 12) = 12

    Appraoch: sum up even or odd positions and compare (Wrong approach)

    T=O(n), S=O(1)
    """
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sum_even = 0
        sum_odd = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                sum_even += nums[i]
            else:
                sum_odd += nums[i]

        return max(sum_even, sum_odd)

    
    # This code cannot pass the case [2,1,1,2]
    # The professional robber can jump or skip more than two houses to maximize the value
    # Output = 3, Expected = 4

# 15. 3Sum (Medium)
# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find three numbers that make zero sum
        return [[val1, val2, val3], ..] # more than one result, do not return its index
    
        * i != j, i != k, and j != k
        * nums[i] + nums[j] + nums[k] == 0

        Example 1:
        nums = [-1,0,1,2,-1,-4], target = 0
    
        sort()
        -4 -1 -1 0 1 2
    
        -4 => target=4 (x)
        -1 => target=1 (0,1), (-1,2) 
        0 => target = 0 (x)
        1 => target = -1 (-1,0)
        2 => target = -2 (x) index must not be duplicated
    
        return [[-1,0,1], [-1,-1,2]]

        Approach:
        First, sort nums array list
        Fix one of the numbers and loop (@ Hint 1)
        Two-pointer approach is chosen inside of the loop

        T=O(n**2), S=O(n**2) upperbound
        """

        nums.sort()
        s = set()

        for i in range(len(nums)):
            j = i + 1  # go to right
            k = len(nums) - 1 # go to left 

            while (j < k):
                t_sum = nums[i] + nums[j] + nums[k]
                if t_sum == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif t_sum < 0:
                    j += 1
                else:
                    k -= 1

        return list(s)

# 15. 3Sum (Medium)
# https://leetcode.com/problems/3sum

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find a combination of numbers that makes sum to 0
        return all the triplets, no duplicates allowed

        Example:
        nums = [-1,0,1,2,-1,-4]
        return [[-1,-1,2],[-1,0,1]]

        Approach:
        First, sort nums array list
        Fix one of the numbers and loop (@ Hint 1)
        Two-pointer approach is chosen inside of the loop
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

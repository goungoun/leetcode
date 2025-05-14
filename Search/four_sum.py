# 18. 4Sum (Medium)
# https://leetcode.com/problems/4sum/description/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Find unique for numbers such that the sum becomes the target
        return [nums[a], nums[b], nums[c], nums[d]] # return values, not index

        * nums[a] + nums[b] + nums[c] + nums[d] == target

        Example 1:
        nums = [1,0,-1,0,-2,2], target = 0

        return [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

        Example 2:
        nums = [2,2,2,2,2], target = 8

        return [[2,2,2,2]]

        Approach: Two pointer
        Bruth force approach requires four nest for loop which will retult O(n**4)
        To reduce the time complexity, replace two inner loop to use two pointer O(n), it becomes O(n**3)

        T=O(n**3), S=O(n)
        """
        if not nums:
            return []

        n = len(nums)
        ret = set()

        # sort an input to use two pointer.
        # note: It changes the index of each value, but it is not impacting because the problem asked us to return its value, not the index
        nums.sort() 

        for a in range(n):
            for b in range(a+1, n):
                c, d = b+1, n-1
                while c < d: # = is not included because a,b,c, and d are distinct                   
                    f_sum = nums[a] + nums[b] + nums[c] + nums[d]

                    if f_sum == target and len(set([a,b,c,d])) == 4:
                        ret.add((nums[a], nums[b], nums[c], nums[d]))
                        c += 1
                        d -= 1
                    elif f_sum > target:
                        d -= 1
                    else:
                        c += 1
                
        return list(map(list,ret))

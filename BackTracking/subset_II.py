# 90. Subsets II
# https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        List up all possible subsets of a list that contains duplicates
        return power_set

        nums = [1,2,2]
                   [1]            [] 
              [1,2]   [1]       [2]     []
           [1,2,2] [1,2] [1] [2,2] [2]* [2]* []

        return [[1,2,2], [1,2], [1], [2,2], [2], []]

        Approach:
        The same pattern of 78. subset 
        Decision tree of selecting each of the elements or not
        Leaf nodes will be all possible subsets 
        """
        len_nums = len(nums)
        tmp = []
        ret = set()
        
        nums.sort()

        def dfs(i):
            if i == len_nums:
                ret.add(tuple(tmp))
                return

            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()
            dfs(i+1)

        dfs(0)

        # print (f"ret={ret}")

        return list(map(list, ret))

            

# 78. Subsets (Medium)
# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Find all possible subsets from an integer array num
        return all_subsets 

        Approach:
        Decision tree of selecting each of the element or not
        Leaf nodes will be all possible subsets
        No specific condition for prunning

        Example 1:
        nums = [1,2,3]
        i = 0: Select 1 or not              [1]                 []
        i = 1: Select 2 or not       [1,2]       [1]       [2]      []
        i = 2: Select 3 or not  [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []  
        i = 3: append possible sets
        """
        all_subsets = []
        tmp = []

        def recSubsets(i):
            if i == len(nums):
                all_subsets.append(tmp.copy())
                return
            
            # Select
            tmp.append(nums[i])
            recSubsets(i+1)

            # Or not
            tmp.pop()
            recSubsets(i+1)

        recSubsets(0)

        return all_subsets

    def subsets_order(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        all_subsets = []
 
        def dfs(i, tmp=[]):
            if i == -1:
                all_subsets.append(tmp)
                return
            
            dfs(i-1, tmp)
            dfs(i-1, [nums[i]]+tmp)
            
        dfs(len(nums)-1)

        return all_subsets

    def subsets_combination(self, nums: List[int]) -> List[List[int]]:
        """
        Approach:
        Use itertools.combinations

        return [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
        """
        all_subsets = []
        n = len(nums)

        from itertools import combinations
        
        for i in range(n + 1):
            for combo in combinations(nums, i):
                all_subsets.append(list(combo))

        return all_subsets

        
        

### WARNING!! This is for a practice, not a complete solution. Need to complete ?.

# 78. Subsets (Medium)
# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Find all possible subsets from an integer array num
        return l_subsets 

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
        l_subsets = []
        tmp = []

        def recSubsets(i):
            if i == len(nums):
                l_subsets.append(tmp) # Fix here: otherwise it will be empty
                ????? # Fix here: without this no useful base condition.
            
            # Select
            ?????
            recSubsets(i) # Fix here

            # Or not
            ?????
            recSubsets(i) # Fix here

        ????? # Fix here. You were going to call the helper function. Without this it, empty return. 

        return l_subsets

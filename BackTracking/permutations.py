# 46. Permutations (Medium)
# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate permutations from the given array nums
        return permutations
        
        Example 1:
        nums = [1]
        return [[1]]

        Example 2:
        nums = [0,1]
        return [[0,1],[1,0]]

        Example 3:
        nums = [1,2,3]
        i=0:         [1]          [2]             [3]
        i=1:   [1,2]  [1,3]    [2,1] [2,3]     [3,1] [3,2]
        i=2: [1,2,3] [1,3,2]  [2,1,3] [2,3,1] [3,1,2] [3,2,1]

        return [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

        Approach:
        Pick one of the nums and add it to a tmp list
        Go down to a deeper level and select another one and add it to a tmp list
        If tmp is filled with all numbers, append it to the result list
        Go back where it was and remove the value to prepare next iteration

        T=O(n!), S=O(n!)
        """
        if not nums:
            return []
        
        tmp = []
        tmp_set = set() # According to the constraint, all the integers of nums are unique.
        permutations = []
        len_nums = len(nums)

        def dfs():
            if len(tmp) == len_nums:
                permutations.append(tmp.copy())
                return
            
            for n in nums:
                if n not in tmp_set:
                    tmp.append(n)
                    tmp_set.add(n)
                    dfs() # tmp is maintained as a context during the recursive call!
                    tmp.pop()
                    tmp_set.remove(n)

        dfs()

        return permutations

# See also: ./Iterator/permutations.py

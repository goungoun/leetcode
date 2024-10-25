# 46. Permutations (Medium)
# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        List up the possible permutation using nums
        return l_permutations
        
        Example 1:
        nums = [1]
        return [[1]]

        Example 2:
        nums = [0,1]
        return [[0,1],[1,0]]

        Example 3:
        nums = [1,2,3]
        L1           [1]            [2]            [3]
        L2        [1,2] [1,3]    [2,1] [2,3]    [3,1] [3,2]
        L3   [1,2,3]    [1,3,2] [2,1,3][2,3,1] [3,1,2] [3,2,1]

        return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

        Approach:
        Pick one of the nums and add it to a tmp list
        Go down to a deeper level and select another one and add it to a tmp list
        If tmp is filled with all numbers, append it to the result list
        Go back where it was and remove the value to prepare next iteration

        T=O(n!), S=O(n!)
        """
        len_nums = len(nums)
        tmp = []
        tmp_set = set() # According to the constraint, all the integers of nums are unique.
        l_permutations = []

        def dfs():
            if len(tmp) == len_nums:
                l_permutations.append(tmp.copy())
                return
            
            for n in nums:
                if n not in tmp_set:
                    tmp.append(n)
                    tmp_set.add(n)
                    dfs() # tmp is maintained as a context during the recursive call!
                    tmp.pop()
                    tmp_set.remove(n)

        dfs()

        return l_permutations
        

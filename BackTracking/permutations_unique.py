# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        nums might contain duplicates
        return all possible unique permutations

        Approach:
        Add one of the nums and its index as a tuple e.g (i, num), to a tmp list
        Go down to a deeper level and select another one and add it to a tmp list
        If tmp is filled with all numbers, extract the num from the tuple and append it to the result list
        Go back where it was and remove the value to prepare next iteration

        Example:
        L1:         [1]            [1]            [2]
        L2:      [1,1] [1,2]   [1,1] [1,2]    [2,1] [2,1]
        L3:   [1,1,2] [1,2,1] [1,1,2] [1,2,1] [2,1,1] [2,1,1]

        return [1,1,2], [1,2,1], [2,1,1]

        * The solution quick and easy, but only beats 5.08%
        """

        ret = []
        tmp = []

        def dfs():
            if len(tmp) == len(nums):
                tmp2 = [n for _,n in tmp]
                if tmp2 not in ret:
                    ret.append(tmp2)
                return

            for i, num in enumerate(nums):
                if (i,num) not in tmp:
                    tmp.append((i,num))
                    dfs()
                    tmp.pop()

        dfs()

        return ret

# 46. Permutations
# https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate permutations from the given array nums

        Approach: itertools
        The built-in python function returns a list of tuples, it also pass the test cases.
        return [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
        """
        from itertools import permutations
        return list(permutations(nums))

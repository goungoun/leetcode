# 78. Subsets (Medium)
# https://leetcode.com/problems/subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Approach: Bit
        Example:
        nums = [1,2,3]
        mask = 0 (000): []
        mask = 1 (001): [1]
        mask = 2 (010): [2]
        mask = 3 (011): [1, 2]
        mask = 4 (100): [3]
        mask = 5 (101): [1, 3]
        mask = 6 (110): [2, 3]
        mask = 7 (111): [1, 2, 3]
        """
        if not nums:
            return []

        n = len(nums)
        cnt_subsets = 1 << n # 2^n

        ret = []

        for mask in range(cnt_subsets):
            tmp = []
            for j in range(n):
                # if j-th bit is 1, add nums[j] to the subset
                if (mask & (1 << j)) != 0:
                    tmp.append(nums[j])
            ret.append(tmp.copy())
        
        return ret

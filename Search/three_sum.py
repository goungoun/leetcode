# 15. 3Sum
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
        First, sort nums arry list
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

    def threeSum_bak(self, nums: List[int]) -> List[List[int]]:
        """
        Tried dictionary approach like two-sum
        Not applicable. Time Limit Exceeded from a specific case repeating 0
        """
        set_triplets = set()
        list_triplets = []

        d = defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        # i, j, k
        len_num = len(nums)
        for i in range(len_num):
            for j in range(len_num):
                search_val = -(nums[i] + nums[j])
                idx_list = d.get(search_val)
                if idx_list is not None:
                    for k in idx_list:
                        if k and i != j and i != k and j != k:
                            set_triplets.add(tuple(sorted([nums[i], nums[j], search_val])))

        return list(map(list, set_triplets))

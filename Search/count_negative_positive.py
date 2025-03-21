# 2529. Maximum Count of Positive Integer and Negative Integer
# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        """
        Count the number of positive integers and the negative integers and compare
        return max_cnt

        * nums are sorted

        Example 1:
        nums = [-2,-1,-1,1,2,3]
        F F F T T T
        
        cnt_positive = 3
        cnt_negative = 3

        return 3

        Example 2: 
        nums = [-3,-2,-1,0,0,1,2]
        F F F - - T T

        cnt_positive = 2
        cnt_negative = 3

        return 3

        Appproach: Two pointer binary search
        T = O(log n), S = O(1)
        """
        if not nums:
            return 0

        n = len(nums)

        # 1. Count Positive numbers
        l, r = 0, n - 1
        first_positive = -1 

        while l <= r:
            mid = (l+r)//2
            is_positive = (nums[mid] > 0)

            # go to left to find the first one
            if is_positive:
                first_positive = mid
                r = mid - 1
            else:
                l = mid + 1

        cnt_positive = n - first_positive if first_positive > -1 else 0

        # 2. Count negative numbers
        l, r = 0, n - 1
        last_negative = -1

        while l <= r:
            mid = (l+r)//2
            is_negative = (nums[mid] < 0)

            # go to right to find the last one
            if is_negative:
                last_negative = mid
                l = mid + 1             
            else:
                r = mid - 1

        cnt_negative = last_negative + 1 if last_negative > -1 else 0

        #print(f"cnt_positive={cnt_positive}, cnt_negative={cnt_negative}")

        return max(cnt_positive, cnt_negative)

# See also: first_bad_version.py

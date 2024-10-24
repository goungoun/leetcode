# 167. Two Sum II - Input Array Is Sorted (Medium)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers to make target
        return [index1, index2]
        
        Example:
        numbers = [2,7,11,15], target = 9

        Approach: Two index
        Use two index l(left) and r(right)
        Move the index l to the right and index r to the left until find the target

        T=O(n), S=O(1)
        """
        if not numbers and target is None:
            return []

        l, r = 0, len(numbers) -1

        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1,r+1] # non-zero index system
            elif s > target:
                r -= 1
            elif s < target:
                l += 1

        return [-1,-1]
    
    def twoSum_bak(self, numbers: List[int], target: int) -> List[int]:
        """
        Approach:
        Use nested iteration.
        One iteration is for loop, the inside loop is replaced with a binary search call
        T=(n^2) -> T(n*logn)
        S=O(1) 
        """
        if not numbers or target is None:
            return []

        def bin_search(idx:int, search_val:int) -> int:
            """
            search a value given the numbers
            return idx or -1 (if it does not exists)

            T=O(log n), S=O(1)
            """
            l, r = 0, len(numbers)-1
            prv_mid = -1

            while l <= r:
                mid = (r + l) // 2
                if numbers[mid] == search_val and mid != idx:
                    return mid
                elif mid == prv_mid:
                    return -1
                elif numbers[mid] < search_val:
                    l = mid + 1
                elif numbers[mid] > search_val:
                    r = mid - 1
                prv_mid = mid

            return -1

        for i, number in enumerate(numbers):
            search_val = target - number
            j = bin_search(i, search_val)

            if j != -1:
                # The index is not zero base, so +1
                return sorted([i+1, j+1])

        return [-1, -1]


# chk: Does it contain duplicated values?
# chk: Is it allowed same index as a return?

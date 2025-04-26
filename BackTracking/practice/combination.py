### WARNING!! This is for a practice, not a complete solution. Need to complete ?.

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        Generate k combinations from the range 1 to n

        * combination: ignore order such as [1,2] and [2,1] are the same cf. permutations

        Example 1: n < k
        n = 4, k = 2

        k = 1:   [1]              [2]          [3]   [4]
        k = 2: [1,2] [1,3] [1,4]  [2,3] [2,4]  [3,4]  -

        return [[1,2], [1,3], 1,4], [2,3], [2,4], [3,4]]

        Example 2: n = k
        n = 1, k = 1

        return [[1]]

        Approach: Back Tracking with recursions
        When we choose the element, pick the element that is larger than the one itself
        It is because of the order, combinations are unordered not like permutations
        For the base condition, it will stop calling the function when the length of the tmp becomes k
        """
        if not n or not 1 <= n <= 20:
            raise ValueError (f"Input n is not in the valid range 1 <= n <= 20, n={n}")

        if not k or not 1 <= k <= n:
            raise ValueError (f"Input k is not in the valid range 1 <= k <= n, k={k}")

        l_combinations = []
        tmp = []

        def dfs(start):
            if len(tmp) == k:
                l_combinations.append(?) # Complete Here
                return

            for i in range(start, n+1): # [start, n]
                tmp.append(i)
                ??? # Complete Here
                tmp.pop()
            
        dfs(1)

        return l_combinations




        

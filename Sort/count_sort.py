# 1051. Height Checker
# https://leetcode.com/problems/height-checker

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Check heights if it has the non-decreasing (=increasing) order
        return cnt_mismatch

        Example:
        heights  : [1,1,4,2,1,3]
        expected : [1,1,1,2,3,4]
        
        return 3

        Approach:
        The constraint of the hight, 1 <= heights[i] <= 100, is eligible for count sort
        This is about student's height, if initilized using array most of them will be sparse
        I selected a dictionary for this reason, but it is not a stable sort anymore. 
        """
        if not heights:
            return 0

        counter = defaultdict(int) # key: height, value: cnt
        min_height, max_height = 100, 0
        for height in heights:
            counter[height] += 1
            if height > max_height:
                max_height = height
            elif height < min_height:
                min_height = height

        idx = 0
        cnt_mismatch = 0
        for i in range(min_height, max_height+1): # for i in range(1,101):
            height, cnt = i, counter[i]
            for _ in range(cnt):
                if heights[idx] != height:
                    cnt_mismatch += 1
                idx += 1
        
        return cnt_mismatch

    def heightChecker_array(self, heights: List[int]) -> int:
        if not heights:
            return 0

        # O(k)
        counter = [0]*(max(heights)+1)
        
        # O(n)
        for height in heights:
            counter[height] += 1

        # O(n+k)
        expected = []
        for i in range(len(counter)): # for i in range(1,101):
            expected.extend([i]*counter[i])
        
        # O(n)
        cnt_wrong_order = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                cnt_wrong_order += 1

        return cnt_wrong_order

    def heightChecker_sorted(self, heights: List[int]) -> int:
        return sum([1 if x!=y else 0 for x, y in zip(heights, sorted(heights))])


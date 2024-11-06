# 1051. Height Checker
# https://leetcode.com/problems/height-checker

class Solution:
    def _radixSort(self, nums: List[int]) -> List[int]:
        """
        T=O(nk)
        S=O(n+k)
        """
        n = len(nums)
        
        buckets = [deque() for _ in range(10)]
        
        max_val = max(nums)
        queue = deque(nums)
        digit = 1 
        
        while max_val >= digit: 
            while queue:
                num = queue.popleft()
                buckets[(num // digit) % 10].append(num) 
            
            for bucket in buckets:
                while bucket:
                    queue.append(bucket.popleft())

            digit *= 10

        return list(queue)

    def heightChecker(self, heights: List[int]) -> int:
        """
        T=O(nk)
        S=O(n+k)
        """
        if not heights:
            return 0
        
        n = len(heights)
        expected = self._radixSort(heights)

        return sum(1 for i in range(n) if heights[i]!=expected[i])

    # referenced radix sort code: https://10000cow.tistory.com/entry/%EC%A0%95%EB%A0%AC-7-%EA%B8%B0%EC%88%98-%EC%A0%95%EB%A0%ACradix-sort

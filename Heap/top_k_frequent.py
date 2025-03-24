# 347. Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
from heapq import heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Top K most frequent elements
        return list_elements

        Example:
        nums = [1,1,1,2,2,3], k = 2
        counter = {1:3, 2:2, 3:1}
        return [1,2]

        T=O(k log n), S=O(n)
        Beats 76.22%
        """
        if not nums or not k:
            return []

        res = []
        counter = Counter(nums)
        
        h = [(-cnt, num) for num, cnt in counter.items()]
        heapify(h)
        
        while k > 0:
            _, num = heappop(h)
            res.append(num)
            k -= 1

        return res

# See also: ../Sort/top_k_frequent.py

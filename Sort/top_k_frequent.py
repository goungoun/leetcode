# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Top k most frequent element

        Approach:
        Count element for the frequency
        Sort the nums based on the frequency

        T=O(n log n), S=(n)
        """
        d = Counter(nums)
        l = sorted(d.items(), key=lambda x: x[1], reverse=True)

        return [key for key, cnt in l[:k]]

# See also: ../Heap/top_k_frequent.py

# 23. Merge k Sorted Lists (Hard)
# https://leetcode.com/problems/merge-k-sorted-lists

from heapq import heappush, heappop


#### Warning!!! This is a buggy code for a practice

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge sorted linked-list more than multiple
        return head_node

        Example 1: Normal case
        lists = [[_,_,_],[_,_,_],[_,_]]
        1 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
        return head_node (of the 1)

        Example 2: empty case
        lists = []
        return None

        Example 3: one case
        lists = [[1,2,3,4,5],[],[]] or lists = [[],[],[1,2,3,4,5]]
        1 -> 2 -> 3 -> 4 -> 5
        return head_node (of the 1)
        """
        if not lists:
            return None

        h = []
        dummy = ListNode()
        curr = dummy

        for i, node in enumerate(lists):
            if node:
                heappush(h, (node.val, i, node))
                node = node.next

        while h:
            _, i, node = heappop(h)
            curr.next = node
            curr = curr.next

            for node in lists:
                if node:
                    heappush(h, (node.val, i, node))
                    node = node.next

        return dummy.next
      
#### Warning!!! This is a buggy code for a practice
"""
TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
    heappush(h, (node.val, i, node))
Line 50 in mergeKLists (Solution.py)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ret = Solution().mergeKLists(param_1)
Line 82 in _driver (Solution.py)
    _driver()
Line 97 in <module> (Solution.py)
"""

# 23. Merge k Sorted Lists (Hard)
# https://leetcode.com/problems/merge-k-sorted-lists

from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        h = [] # min heap by default
        for i, start_node in enumerate(lists):
            if start_node:
                heappush(h, (start_node.val, i, start_node))

        dummy = ListNode()
        curr = dummy

        while h:
            _,i, node = heappop(h)
            curr.next = node
            curr = curr.next

            if node.next:
                heappush(h, (node.next.val, i, node.next))

        return dummy.next

# Referenced the solution by Greg Hogg
# https://www.youtube.com/watch?v=RyrVWP76lVo

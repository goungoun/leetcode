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
        """
        Merge linked-lists sorted in ascending order.

        Approach: Use heap to compare values more then two
        Add first nodes to the heap
        Iterate through the heap and heap pop to get the min_node
        Add another min_node to the heap
        
        T=O(nlogk), beats 96.09%
        S=(k), beats 77.54%
        """
        if not lists:
            return None

        h = [] # min heap by default
        for i, node in enumerate(lists):
            if node:
                heappush(h, (node.val, i, node))

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

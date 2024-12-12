# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Approach: Use heap sort
        Iterate the all node values in the list and build a min heap
        Pop values from the heap and make new list nodes
        Return the first node

        T=O(nlogn)
        S=O(n)
        """
        if not lists:
            return None

        # add all values to the min heap h
        h = []
        heapify(h)
        
        for node in lists:
            while node:
                heappush(h, node.val)
                node = node.next

        # get a value from the heap
        dummy = ListNode(None)
        curr = dummy

        while h:
            val = heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next
      

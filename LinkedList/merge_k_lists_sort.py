# 23. Merge k Sorted Lists (Hard)
# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l = []

        for li in lists:
            curr = li
            while curr:
                l.append(curr.val)
                curr = curr.next

        l.sort() # O(n log n)

        dummy = ListNode()
        curr = dummy

        for val in l:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

# This is not the best solution
# See also: merge_k_lists_heap.py

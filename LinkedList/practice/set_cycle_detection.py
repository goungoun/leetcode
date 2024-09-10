# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        If you don't know about Floyd's Cycle Detection Algorithm, also known as the "tortoise and hare, we can use set to detect cycle.
        FYI. Different node can have the same value.
        """
        visited = set()
        curr = head
        
        while curr:
            if curr in visited:
                return True
            else:
                visited.add(?) # Fix here
                curr = curr.next

        return False

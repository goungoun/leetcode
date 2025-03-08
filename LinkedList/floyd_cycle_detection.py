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
        Floyd's Cycle Detection Algorithm, also known as the "tortoise and hare"

        Example 1: Cycle exists
        head = [3,2,0,-4], pos = 1
        +1: 3 2 0 "-4" 2 0 -4 2 ...
        +2: 3 0 2 "-4" 0 2 ...
        return True

        Example 2: Cycle exists
        head = [1,2], pos = 0
        +1: 1 2 "1" 2 1 2 1 2 ...
        +2: 1 1 "1" 1 1 1 1 1 ...
        return True

        Example 3: No cycle (pos= -1)
        head = [1], pos = -1
        +1: 1 <End>
        +2: 1 <End>
        return False
        """
        slow, fast = head, head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

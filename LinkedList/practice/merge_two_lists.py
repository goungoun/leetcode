# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#### Warning!!! This is a buggy code for a practice

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        # Fix This: we need more variable.. it will end up being empty
        dummy = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                dummy.next = list1            
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next

            dummy = dummy.next

            #print(dummy)

        # Fix This: Use the test case to debug this code. list1 =[1,2,4], list2=[1,3,4]
        if not list1:
            dummy.next = list1

        if not list2:
            dummy.next = list2

        return dummy.next

        

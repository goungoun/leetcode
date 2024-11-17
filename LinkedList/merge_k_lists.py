# 23. Merge k Sorted Lists (Hard)
# https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge Sorted Lists more than two
        return head, the head of the merged sorted list

        Approach:
        Step 1 - Merge two sorted Array
        Step 2 - Loop other lists and repeat Step 1

        Example:
        lists = [[1,4,5],[1,3,4],[2,6]]
        l1 = [1,4,5], l2 = [1,3,4]
        -,-
        l1 = [1,1,3,4,4,5], l2 = [2,6]
        -,-
        return [1,1,2,3,4,4,5,6]
        """
        if not lists:
            return None
        
        l = lists[0]
        for i in range(1,len(lists)):
            l = self.merge2Lists(l,lists[i])
        return l

    def merge2Lists(self, list1:Optional[ListNode], list2:Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        curr = ListNode()
        dummy = curr

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return dummy.next

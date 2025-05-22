# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Merge two sorted list
    return head

    Example 1:
    list1 = [1,2,4], list2 = [1,3,4]

    -,-,-
    -,-,4

    (1,1) 1
    (2,1) 1
    (2,3) 2
    (4,3) 3
    (4,4) 4
    -     4

    1->1->2->3->4->4
    
    return head

    Example 2: the lists are all empty
    list1 = [], list2 = []

    return None

    Example 3: one of the lists is empty
    list1 = [], list2 = [0]

    return head (head of the list2)

    Approach: Do not create new nodes to save space. Reuse nodes and change the next pointer
    Make one dummy node and also create the current point
    Iterate one of the list list1 or list2 while picking up the smallest element
    Connect small one to the next node
    Make sure to move curr, list1 or list 2.
    Repeat until one of the list is used up to the end
    If necessary, link up the current point to the remained list

    T=O(m+n), S=O(1)
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases: Example 2 and Example 3
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
            
        dummy = ListNode()
        curr = dummy
        
        while list1 and list2:
            # non decreasing order
            if list1.val <= list2.val: 
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # if the lists are not reaching to the end, it is not None
        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        head = dummy.next
        return head

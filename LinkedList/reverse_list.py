# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse Linked List
        return the head of the reversed list

        Steps:
        1) Keep the next node before update the next value
        2) Update the curr.next to be able to point to the previous node 
        3) Go to the next using the variable from 1) and Repeats 1) and 2)

        Examples:
        head = [1,2,3,4,5]
        1->2->3->4->5

        None<-1
        1<-2
        2<-3
        3<-4
        4<-5
        None <End>

        head = [1,2]
        1->2

        None<-1
        1<-2
        None

        head = []
        None
        """

        curr = head
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr= tmp

        return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None: 
            return head
        
        rev_list = head
        head = head.next
        rev_list.next = None
        while head is not None:
            temp = head.next
            head.next = rev_list
            rev_list = head
            head = temp
        
        return rev_list
        
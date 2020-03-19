# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        dummy_pointer = dummy_head
        l1_pointer = l1
        l2_pointer = l2
        while l1_pointer is not None and l2_pointer is not None:
            if l1_pointer.val < l2_pointer.val:
                dummy_head.next = l1_pointer
                l1_pointer = l1_pointer.next
            else:
                dummy_head.next = l2_pointer
                l2_pointer = l2_pointer.next
            dummy_head = dummy_head.next
        
        while l1_pointer is not None:
            dummy_head.next = l1_pointer
            l1_pointer = l1_pointer.next
            dummy_head = dummy_head.next
        
        while l2_pointer is not None:
            dummy_head.next = l2_pointer
            l2_pointer = l2_pointer.next
            dummy_head = dummy_head.next
        
        if dummy_pointer.next:
            return dummy_pointer.next
        
        return None
            
                
                
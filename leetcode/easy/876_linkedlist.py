# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
            
            
    
    def middleNode1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 
        start = head 
        while head:
            n += 1 
            head = head.next
            
        head = start 
        
        idx = 0
        while head:
            if idx == n // 2:
                return head 
            idx += 1 
            head = head.next
            
        

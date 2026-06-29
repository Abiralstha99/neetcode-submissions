# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # First create a dummy head 
        dummy = ListNode(0, head)
        # initialise slow and fast pointer
        slow = fast = dummy
        for i in range(0,n):
            fast = fast.next 
        
        # Until fast reaches EOL, iterate
        while (fast.next != None):
            fast = fast.next
            slow = slow.next

        # Now slow is at the node just one before the 'to remove node'
        slow.next = slow.next.next
        return dummy.next

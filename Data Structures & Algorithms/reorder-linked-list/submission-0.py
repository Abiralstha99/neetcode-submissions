# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # First divide the list
        slow,fast = head,head.next
        first = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        # the slow pointer's next would be the second head
        second = slow.next
        # Now reverse the second list
        prev = None
        slow.next = None
        while(second):
            tmp = second.next 
            second.next = prev
            prev = second
            second = tmp
        second = prev
        # Now merge two list
        while(second):
            tmp = first.next
            first.next = second
            tmp2 = second.next 
            second.next = tmp
            first = tmp
            second = tmp2

        

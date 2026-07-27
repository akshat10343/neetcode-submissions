# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        cur = head
        check = head
        while cur:
            if cur.next is None:
                return False
            cur = cur.next
            if cur == check:
                return True
            if cur.next is None:
                return False
            cur = cur.next
            if cur == check:
                return True
            check = check.next
        return False
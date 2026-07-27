# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        cur = dummy
        check = dummy
        for i in range(n):
            check = check.next
        if check.next is None:
            head = head.next
            return head

        while head:
            if check.next is None:
                cur.next = cur.next.next
                break
            else:
                check = check.next
                cur = cur.next
        return head
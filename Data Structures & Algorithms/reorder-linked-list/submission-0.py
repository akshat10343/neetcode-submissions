# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        cur = head
        while cur:
            l.append(cur)
            cur = cur.next

        left = 0
        right = len(l) - 1
        while left < right:
            l[left].next = l[right]
            left = left + 1
            if left == right:
                break
            l[right].next = l[left]
            right = right - 1

        l[right].next = None
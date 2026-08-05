# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            if  len(lists) <= 1:
                return None
        h = []
        for i in lists:
            if i is None:
                continue
            j = i
            while True:
                if j.next is not None:
                    heapq.heappush(h,j.val)
                    j = j.next
                elif j.next == None:
                    heapq.heappush(h,j.val)
                    break
        self.head = None
        if len(h) == 0:
            return None
        head = ListNode(heapq.heappop(h))
        current = head
        for i in range(len(h)):
            current.next = ListNode(heapq.heappop(h))
            current = current.next
        return head


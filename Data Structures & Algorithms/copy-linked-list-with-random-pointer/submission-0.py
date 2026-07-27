"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None: None}

        dummy = Node(0)
        cur = dummy
        check = head

        # pass 1: create every copy, chain the next pointers, record the pairing
        while head:
            copy = Node(head.val)
            d[head] = copy
            cur.next = copy
            cur = cur.next
            head = head.next

        # pass 2: every copy exists now, so the random lookups always hit
        while check:
            d[check].random = d[check.random]
            check = check.next

        return dummy.next
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.l = {}
        self.cap = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key not in self.l:
            return -1
        else:
            dummy = self.l[key]
            dummy.prev.next = dummy.next
            dummy.next.prev = dummy.prev
            dummy.prev = self.tail.prev
            self.tail.prev.next = dummy
            dummy.next = self.tail
            self.tail.prev = dummy
        return self.l[key].val

    def put(self, key: int, value: int) -> None:
        if key not in self.l:
            dummy = Node(key, value)
            dummy.prev = self.tail.prev
            self.tail.prev.next = dummy
            dummy.next = self.tail
            self.tail.prev = dummy
            self.l[key] = dummy
            if len(self.l) > self.cap:
                self.l.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
        else:
            dummy = self.l[key]
            dummy.val = value
            dummy.prev.next = dummy.next
            dummy.next.prev = dummy.prev
            dummy.prev = self.tail.prev
            self.tail.prev.next = dummy
            dummy.next = self.tail
            self.tail.prev = dummy
import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == 0 or num <= (self.min_heap[0]*(-1)):
            heapq.heappush(self.min_heap, num*(-1))
        else:
            heapq.heappush(self.max_heap, num)

        if len(self.min_heap) > len(self.max_heap) + 1:
            temp = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, temp*(-1))
        if len(self.max_heap) > len(self.min_heap) + 1:
            temp = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, temp*(-1))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0]*(-1) + self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]*(-1)
        elif len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0]
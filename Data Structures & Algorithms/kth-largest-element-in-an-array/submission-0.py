from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = []
        for i in nums:
            heappush(h,(i*-1))
        temp = h[0]
        for i in range(k):
            temp = heappop(h)
        return temp*-1

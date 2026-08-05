import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        h = []
        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(h, [dist, x, y])
        result = []
        for _ in range(k):
            dist, x, y = heapq.heappop(h)
            result.append([x, y])
        return result


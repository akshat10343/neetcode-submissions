class Solution:
    def leastInterval(self, tasks, n):
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]  # negate -> max-heap of counts
        heapq.heapify(heap)
        queue = deque()  # (remaining_count, ready_time)
        time = 0

        while heap or queue:  # keep going while anything's left
            time += 1
            if heap:
                cnt = heapq.heappop(heap) + 1  # run one copy. (+1 because counts
                #   are negative: -3 -> -2 is "used one")
                if cnt != 0:  # still has copies left?
                    queue.append((cnt, time +n))  # ??? = when is it ready again?
            if queue and queue[0][1] == time:  # ??? = is the front one ready NOW?
                heapq.heappush(heap, queue.popleft()[0])

        return time

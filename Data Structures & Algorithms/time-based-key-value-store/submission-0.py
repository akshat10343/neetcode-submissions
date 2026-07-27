class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])
        pass

    def get(self, key: str, timestamp: int) -> str:
        history = self.store[key]
        lo, hi = 0, len(history) - 1
        best = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if history[mid][0] <= timestamp:
                best = history[mid][1]
                lo = mid + 1
            else:
                hi = mid -1
        return best
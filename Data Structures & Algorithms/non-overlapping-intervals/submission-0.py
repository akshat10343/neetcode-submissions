class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        prev_end = float('-inf')  # nothing kept yet
        count = 0
        for s, e in intervals:
            if s >= prev_end:  
                prev_end = e
            else:  
                count += 1
        return count
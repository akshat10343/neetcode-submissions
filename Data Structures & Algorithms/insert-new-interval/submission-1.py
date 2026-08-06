class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if len(intervals) == 0:
            return [newInterval]

        d = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:  # compare STARTS
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)


        for i, j in intervals:
            if d and i <= d[-1][1]:
                if j <= d[-1][1]:
                    pass
                else:
                    d[-1][1] = j
            else:
                d.append([i, j])
        return d
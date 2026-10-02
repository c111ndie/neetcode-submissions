class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        index = len(intervals)
        for i in range(len(intervals)):
            if intervals[i][0] >= start:
                index = i
                break
        intervals = intervals[:index] + [newInterval] + intervals[index:]
        res = []
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            else:
                if intervals[i][0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], intervals[i][1])
                else:
                    res.append(intervals[i])
        return res



        
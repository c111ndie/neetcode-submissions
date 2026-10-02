"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda interval: interval.start)
        if not intervals:
            return True
        i = 1
        max_end = intervals[0].end
        while i < len(intervals):
            if intervals[i].start < max_end:
                return False
            max_end = max(max_end, intervals[i].end)
            i += 1
        return True

# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x:x[0])
        c, p = 0, intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < p:
                c += 1
                p = min(p, intervals[i][1])
            else:
                p = intervals[i][1]
        return c
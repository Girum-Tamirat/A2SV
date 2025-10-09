# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        a = []
        for time in timePoints:
            hh = int(time[0:2]) * 60
            mm = int(time[3:5])
            t = hh + mm
            a.append(t)
        a.sort()
        for i in range(1, len(a)):
            if a[i] == a[i-1]: return 0
        b = []
        for i in range(len(a)-1):
            b.append(a[i+1]-a[i])
        b.append(1440+a[0]-a[-1])
        return min(b)
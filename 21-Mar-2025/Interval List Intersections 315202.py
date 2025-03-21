# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            m = max(firstList[i][0], secondList[j][0])
            n = min(firstList[i][1], secondList[j][1])
            if m <= n:
                ans.append([m, n])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return ans
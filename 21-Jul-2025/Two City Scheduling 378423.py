# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1]-x[0])
        c = 0
        for i in range(len(costs)//2):
            c += costs[i][1]
        for i in range(len(costs)//2, len(costs)):
            c += costs[i][0]
        return c
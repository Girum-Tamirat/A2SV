# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        gtotal = sum(gas)
        ctotal = sum(cost)
        if gtotal < ctotal:
            return -1
        strt = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                strt = i + 1
                tank = 0
        return strt

        
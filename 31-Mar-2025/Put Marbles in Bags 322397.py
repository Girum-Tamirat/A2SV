# Problem: Put Marbles in Bags - https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        p = []
        for i in range(len(weights) - 1):
            p.append(weights[i] + weights[i+1])
        p.sort()
        mn = sum(p[:k-1])
        mx = sum(p[-(k-1):])
        return mx - mn
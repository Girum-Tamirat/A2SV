# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(x):
            u, c = 1, 0
            for w in weights:
                if c+w > x:
                    u+=1
                    c=0
                c += w
            return u<=days
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l+r)//2
            if can_ship(m):
                r = m
            else:
                l = m+1
        return l
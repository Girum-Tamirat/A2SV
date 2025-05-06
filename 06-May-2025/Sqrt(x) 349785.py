# Problem: Sqrt(x) - https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        if x < 2:
            return x
        while l < r:
            m = l+(r-l)//2
            if m*m <= x:
                l = m+1
            else:
                r = m
        return l-1
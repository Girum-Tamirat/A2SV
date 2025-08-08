# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0] * 38
        f[1] = f[2] = 1
        for i in range(3, n+1):
            f[i]=f[i-1]+f[i-2]+f[i-3]
        return f[n]

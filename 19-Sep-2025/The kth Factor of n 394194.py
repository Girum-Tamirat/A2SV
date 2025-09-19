# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f = []
        for i in range(1, n+1):
            if n%i==0: f.append(i)
        return f[k-1] if len(f)>=k else -1
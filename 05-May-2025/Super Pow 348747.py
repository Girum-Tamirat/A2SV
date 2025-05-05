# Problem: Super Pow - https://leetcode.com/problems/super-pow/description/

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        def helper(b):
            if not b:
                return 1
            last = b.pop()
            part1 = pow(self.superPow(a, b), 10, mod)
            part2 = pow(a, last, mod)
            return (part1 * part2) % mod
        return helper(b.copy())
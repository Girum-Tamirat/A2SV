# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a ** 2 <= c:
            b = sqrt(c - a ** 2)
            if b == int(b):
                return True
            a += 1
        return False
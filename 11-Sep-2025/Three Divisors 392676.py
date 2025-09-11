# Problem: Three Divisors - https://leetcode.com/problems/three-divisors/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def isThree(self, n: int) -> bool:
        c = 0
        for i in range(2, n):
            if n%i==0:
                c += 1
        return True if c==1 else False
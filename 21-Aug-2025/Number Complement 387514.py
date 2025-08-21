# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        b = []
        def change(x):
            if x<=1:
                b.append(x)
                return
            change(x//2)
            b.append(x%2)
        change(num)
        for i in range(len(b)):
            if b[i]==0: b[i]=1
            else: b[i]=0
        b.reverse()
        a = []
        for i in range(len(b)):
            a.append(b[i]*2**i)
        return sum(a)
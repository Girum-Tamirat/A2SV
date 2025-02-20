# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        elif n<10:
            return False
        else:
            sum = 0
            while n > 0:
                t = n % 10
                sum += t**2
                n = n // 10
            return self.isHappy(sum)
                

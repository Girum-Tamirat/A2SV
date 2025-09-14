# Problem: Prime Palindrome - https://leetcode.com/problems/prime-palindrome/description/?envType=problem-list-v2&envId=number-theory

class Solution:
    def primePalindrome(self, n: int) -> int:
        def isprime(n):
            if n<2: return False
            if n%2==0: return n==2
            i=3
            while i*i<=n:
                if n%i==0: return False
                i+=2
            return True
        def ispalindrome(n):
            s=str(n)
            return s==s[::-1]
        if n<=11:
            for x in range(n, 12):
                if isprime(x) and ispalindrome(x):
                    return x
        for length in range(1, 6): 
            start = 10**(length - 1)
            end = 10**length
            for half in range(start, end):
                s = str(half)
                pal = int(s + s[-2::-1]) 
                if pal >= n and isprime(pal):
                    return pal
# Problem: Smallest Value After Replacing With Sum of Prime Factors - https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factors(num):
            factors = []
            d = 2
            while num % d == 0:
                factors.append(d)
                num //= d
            d = 3
            while d * d <= num:
                while num % d == 0:
                    factors.append(d)
                    num //= d
                d += 2
            if num > 1:
                factors.append(num)
            return factors

        def isprime(num):
            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for i in range(3, int(math.sqrt(num)) + 1, 2):
                if num % i == 0:
                    return False
            return True

        while not isprime(n):
            factors = prime_factors(n)
            new_n = sum(factors)
            if new_n == n:
                break
            n = new_n
        return n

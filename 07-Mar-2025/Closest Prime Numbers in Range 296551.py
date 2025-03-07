# Problem: Closest Prime Numbers in Range - https://leetcode.com/problems/closest-prime-numbers-in-range/

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False  

        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False
        
        primes = [num for num in range(left, right + 1) if sieve[num]]

        if len(primes) < 2:
            return [-1, -1]

        min_gap = float('inf')
        result = []

        for i in range(len(primes) - 1):
            gap = primes[i + 1] - primes[i]
            if gap < min_gap:
                min_gap = gap
                result = [primes[i], primes[i + 1]]

        return result

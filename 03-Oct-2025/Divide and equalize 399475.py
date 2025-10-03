# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

import sys
import math

def sieve(limit=10**6):
    spf = list(range(limit+1))  # smallest prime factor
    for i in range(2, int(limit**0.5)+1):
        if spf[i] == i:
            for j in range(i*i, limit+1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

spf = sieve()

def factorize(x):
    factors = {}
    while x > 1:
        p = spf[x]
        cnt = 0
        while x % p == 0:
            x //= p
            cnt += 1
        factors[p] = cnt
    return factors

def solve():
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx:idx+n])); idx += n
        primes = {}
        for a in arr:
            f = factorize(a)
            for p, c in f.items():
                primes[p] = primes.get(p, 0) + c
        ok = True
        for total in primes.values():
            if total % n != 0:
                ok = False
                break
        out.append("YES" if ok else "NO")
    print("\n".join(out))

if __name__ == "__main__":
    solve()

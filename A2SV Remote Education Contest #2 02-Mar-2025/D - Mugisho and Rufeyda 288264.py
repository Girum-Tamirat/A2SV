# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

n, t = map(int, input().split())
lower = 10 ** (n - 1)
upper = (10 ** n) - 1

# Calculate the smallest multiple of t >= lower
q = (lower + t - 1) // t
candidate = q * t

if candidate <= upper:
    print(candidate)
else:
    print(-1)
# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())
factors = [0] * (n + 1)
for p in range(2, n + 1):
    if factors[p] == 0:
        for multiple in range(p, n + 1, p):
            factors[multiple] += 1
count = 0
for x in range(2, n + 1):
    if factors[x] == 2:
        count += 1
print(count)
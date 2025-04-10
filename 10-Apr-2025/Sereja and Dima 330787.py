# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())
c = list(map(int, input().split()))
s, d, i, j, t = 0, 0, 0, n-1, 0
while i <= j:
    if c[i] > c[j]:
        m = c[i]
        i += 1
    else:
        m = c[j]
        j -= 1
    if t % 2 == 0:
        s += m
    else:
        d += m
    t += 1
print(s,d)
# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = map(int, input().split())
a = list(map(int, input().split()))
def books(n, t, a):
    i, c, m = 0, 0, 0
    for j in range(n):
        c += a[j]
        while c > t:
            c -= a[i]
            i += 1
        m = max(m, j - i + 1)
    return m
print(books(n, t, a))
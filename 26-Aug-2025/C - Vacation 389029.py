# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())
a, b, c = [], [], []

for _ in range(N):
    x, y, z = map(int, input().split())
    a.append(x)
    b.append(y)
    c.append(z)

dp0, dp1, dp2 = a[0], b[0], c[0]

for i in range(1, N):
    new_dp0 = a[i] + max(dp1, dp2)
    new_dp1 = b[i] + max(dp0, dp2)
    new_dp2 = c[i] + max(dp0, dp1)
    
    dp0, dp1, dp2 = new_dp0, new_dp1, new_dp2

print(max(dp0, dp1, dp2))

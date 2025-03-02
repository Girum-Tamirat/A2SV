# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

s, n = map(int, input().split())
dragons = []
for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))

dragons.sort()

for x, y in dragons:
    if s > x:
        s += y
    else:
        print("NO")
        exit()

print("YES")
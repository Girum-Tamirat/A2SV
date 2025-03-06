# Problem: D - Great Photographer - https://codeforces.com/gym/590201/problem/D

n, x0 = map(int, input().split())
starts = []
ends = []

for _ in range(n):
    a, b = map(int, input().split())
    starts.append(min(a, b))
    ends.append(max(a, b))

max_start = max(starts)
min_end = min(ends)

if max_start > min_end:
    print(-1)
else:
    if x0 < max_start:
        print(max_start - x0)
    elif x0 > min_end:
        print(x0 - min_end)
    else:
        print(0)
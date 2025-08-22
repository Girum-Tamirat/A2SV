# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

n = int(input())
for _ in range(n):
    a = int(input())
    if a == 1:
        print(3)
    elif a & (a - 1) == 0:
        print(a + 1)
    else:
        print(a & -a)

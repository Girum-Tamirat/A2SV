# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())

for r in range(1, n+1):
    if r % 2 == 1:
        print('#' * m)
    else:
        if r % 4 == 0:
            print('#' + '.' * (m-1))
        else:
            print('.' * (m-1) + '#')
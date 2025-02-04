# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import math

def number_of_flagstones(n, m, a):
    fl = math.ceil(n / a)
    fw = math.ceil(m / a)

    return fl * fw
if __name__ == '__main__':
    n, m, a = map(int, input().split())
    print(number_of_flagstones(n, m, a))
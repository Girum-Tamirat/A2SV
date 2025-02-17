# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

def barkingpassword(p, n, c):
    if p in c:
        return "YES"
    for i in range(n):
        for j in range(n):
            if c[i][1] == p[0] and c[j][0] == p[1]:
                return "YES"
    return "NO"
p = input()
n = int(input())
c = [input() for _ in range(n)]

result = barkingpassword(p, n, c)

print(result)

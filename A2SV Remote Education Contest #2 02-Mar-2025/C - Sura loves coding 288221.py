# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

n = int(input())
s = input()
org = []
for i in range(n):
    pos = i // 2
    org.insert(pos, s[n - i - 1])
print("".join(org))
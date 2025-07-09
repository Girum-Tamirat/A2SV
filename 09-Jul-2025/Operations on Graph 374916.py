# Problem: Operations on Graph - https://www.eolymp.com/en/contests/9060/problems/78602

# example below, replace it with your solution
n = int(input())
matrix = [list(map(int, input().split()))for _ in range(n)]
s, k= [], []
for i in range(n):
    iss, isk = True, True
    for j in range(n):
        if matrix[j][i]==1:
            iss=False
        if matrix[i][j]==1:
            isk=False
    if iss: s.append(i+1)
    if isk: k.append(i+1)
print(len(s), *s)
print(len(k), *k)
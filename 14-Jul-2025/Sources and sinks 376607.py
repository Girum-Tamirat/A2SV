# Problem: Sources and sinks - https://basecamp.eolymp.com/en/problems/3986

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
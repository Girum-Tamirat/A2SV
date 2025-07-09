# Problem: From adjacency list to adjacency matrix - https://basecamp.eolymp.com/en/problems/3982

n = int(input())
desc = [list(map(int, input().split())) for _ in range(n)]
res = [[0] * n for _ in range(n)]
for i in range(n):
    for v in desc[i][1:]:
        res[i][v - 1] = 1
for row in res:
    print(*row)
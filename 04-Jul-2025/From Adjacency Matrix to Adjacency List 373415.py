# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

# example below, replace it with your solution
n = int(input())
am = [list(map(int, input().split()))for _ in range(n)]
for i in range(n):
    edges = []
    for j in range(n):
        if am[i][j]==1:
            edges.append(j+1)
    print(len(edges), *edges)
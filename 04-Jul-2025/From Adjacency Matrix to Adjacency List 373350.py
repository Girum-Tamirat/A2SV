# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

# example below, replace it with your solution
n, m = map(int, input().split())
d = [0]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    d[u]+=1
    d[v]+=1
ud=set(d[1:])
if len(ud)==1: print("YES")
else: print("NO")
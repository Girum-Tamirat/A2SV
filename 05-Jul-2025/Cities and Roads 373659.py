# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

# example below, replace it with your solution
n = int(input())
roads = [list(map(int, input().split()))for _ in range(n)]
c=0
for i in range(n):
    for j in range(i+1, n):
        if roads[i][j]==1:
            c+=1
print(c)
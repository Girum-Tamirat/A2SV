# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
c = 0
j = 0
ans = []
for i in range(n):
    while j < m and arr1[j] < arr2[i]:
        c += 1
        j += 1
    ans.append(c)
print(*ans)
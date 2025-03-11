# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

m, n = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
i = 0
j = 0
ans = []
while i < m and j < n:
    if arr1[i] < arr2[j]:
        ans.append(arr1[i])
        i += 1
    else:
            ans.append(arr2[j])
            j += 1
while i < len(arr1):
    ans.append(arr1[i])
    i += 1
while j < len(arr2):
    ans.append(arr2[j])
    j += 1
print(*ans)
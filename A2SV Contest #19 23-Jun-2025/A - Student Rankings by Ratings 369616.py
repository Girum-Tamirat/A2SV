# Problem: A - Student Rankings by Ratings - https://codeforces.com/gym/617023/problem/A

n = int(input())
rate = list(map(int, input().split()))
pose = [1] * n
for i in range(n):
    for j in range(n):
        if rate[j]>rate[i]:
            pose[i] += 1
print(' '.join(map(str, pose)))
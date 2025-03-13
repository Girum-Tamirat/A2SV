# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

n, a, b = list(map(int, input().split()))
arr = list(map(int, input().split()))
s = sum(arr)
res = sorted(arr[1:])
count = 0
while arr[0] * a / s < b:
    s -= res.pop()
    count += 1
print(count)
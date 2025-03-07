# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def find_x(n, k, arr):
    arr.sort()
    if k == 0:
        return arr[0] - 1 if arr[0] > 1 else -1
    x = arr[k-1]
    if k < n and arr[k] == x:
        return -1
    return x

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(find_x(n, k, arr))

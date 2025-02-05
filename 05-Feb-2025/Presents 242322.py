# Problem: Presents - https://codeforces.com/problemset/problem/136/A

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    result = [0] * n
    for i in range(n):
        result[p[i] - 1] = i + 1
    print(" ".join(map(str, result)))
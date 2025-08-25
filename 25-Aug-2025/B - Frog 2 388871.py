# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def frog2():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [0] + [10**18] * (N - 1) 

    for i in range(1, N):
        dp[i] = min(dp[i-j] + abs(h[i] - h[i-j]) for j in range(1, min(K, i) + 1))

    print(dp[-1])

frog2()

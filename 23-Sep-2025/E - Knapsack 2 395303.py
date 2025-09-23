# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

def knapsack(N, W, items):
    max_value = sum(v for _, v in items)
    
    dp = [float('inf')] * (max_value + 1)
    dp[0] = 0 
    
    for weight, value in items:
        for v in range(max_value, value - 1, -1):
            dp[v] = min(dp[v], dp[v - value] + weight)
    
    for v in range(max_value, -1, -1):
        if dp[v] <= W:
            return v 

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

print(knapsack(N, W, items))
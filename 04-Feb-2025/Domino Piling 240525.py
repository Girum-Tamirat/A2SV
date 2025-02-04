# Problem: Domino Piling - https://codeforces.com/problemset/problem/50/A

def max_dominoes (m, n):
    return (m * n) // 2
if __name__ == '__main__':
    m, n = map(int, input().split())
    print(max_dominoes(m, n))
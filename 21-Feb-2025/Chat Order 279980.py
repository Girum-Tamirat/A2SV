# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

n = int(input())
ins = [input() for _ in range(n)]
seen = {}
for name in ins:
    seen.pop(name, None)
    seen[name] = None
print("\n".join(reversed(seen.keys())))
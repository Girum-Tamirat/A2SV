# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

import sys
from collections import defaultdict

def samedifferences():
    data = sys.stdin.read().split()
    
    t = int(data[0]) 
    index = 1
    result = []
    
    for _ in range(t):
        n = int(data[index]) 
        a = list(map(int, data[index + 1 : index + 1 + n])) 
        index += n + 1 
        
        d = defaultdict(int)
        c = 0
        
        for i in range(n):
            key = a[i] - i 
            c += d[key] 
            d[key] += 1 
            
        result.append(str(c))
    
    print("\n".join(result))

if __name__ == "__main__":
    samedifferences()
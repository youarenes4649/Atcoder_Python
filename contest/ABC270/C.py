import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
n,x,y = map(int,input().split())
L = [0]*(n+1)
D = defaultdict(list)
for _ in range(n-1):
    a,b = map(int,input().split())
    D[a].append(b)
    D[b].append(a)
    L[a] = 1
    L[b] = 1
M = []
def dfs(now):
    
    M.append(now)
    L[now] = 0
    
    for nxt in D[now]:
        
        if nxt == y:
            M.append(y)
            print(*M)
            exit()
        else: 
            if L[nxt]==1:
                dfs(nxt)
                M.pop()

dfs(x)

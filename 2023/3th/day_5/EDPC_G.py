import sys
sys.setrecursionlimit(10 ** 7)

N,M = map(int,input().split())
g = [[] for _ in range(N)]
for _ in range(M):
    x,y = map(int,input().split())
    g[x - 1].append(y - 1)
    
dp = [0] * N #メモ化されている

def memo(u):
    if dp[u] != 0:
        return dp[u]
    for to in g[u]:
        dp[u] = max(dp[u],memo(to) + 1)
    return dp[u]
    
ans = 0
for i in range(N):
    ans = max(ans,memo(i))
print(ans)
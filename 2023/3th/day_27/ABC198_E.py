import sys
sys.setrecursionlimit(10 ** 7)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import defaultdict
N = ii()
C = li()
edge = [[] * N for _ in range(N)]
for _ in range(N-1):
    a,b = mi()
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
    
ans = []
seen = [False] * (N)
color = defaultdict(int)
def dfs(x):
    global ans
    seen[x] = True
    if color[C[x]] == 0:
        ans.append(x + 1)
    color[C[x]] += 1
    for to in edge[x]:
        if seen[to]:
            continue
        dfs(to)
    color[C[x]] -= 1

dfs(0)
ans.sort()
for a in ans:
    print(a)
    
        

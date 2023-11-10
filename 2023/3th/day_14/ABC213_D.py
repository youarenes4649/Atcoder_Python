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
 

N = ii()
edge = [[] * N for _ in range(N)]
ans = []
seen = [False] * N
def dfs(x):
    global ans
    seen[x] = True
    ans.append(x + 1)
    for to in edge[x]:
        if seen[to]:
            continue
        dfs(to) #これがおわったら親ノードに戻ってくる
        ans.append(x+1)
    
        
for _ in range(N-1):
    a,b = mi()
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)
for i in range(N):
    edge[i].sort()
        
dfs(0)
print(*ans)

        

import sys
sys.setrecursionlimit(10**7)
ans = 0

def dfs(x):
    global ans
    seen[x] = True
    ans += 1

    if ans >=10**6+10:
        print(10**6)
        exit()
    for nx in edge[x]:
        if seen[nx]:
            continue
        dfs(nx)
        seen[nx] = False #ここにつけること　終わった後だから
    
ans = 0
N,M = map(int,input().split())
edge = [[]* N for _ in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)

seen = [False] * (N)
dfs(0)
print(ans)
    
     

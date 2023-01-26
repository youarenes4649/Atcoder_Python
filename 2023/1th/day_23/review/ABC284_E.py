
import sys
sys.setrecursionlimit(10**7)

def dfs(x):
    global cnt
    seen[x] = True
    cnt += 1
    if cnt > 10**6:
        print(10**6)
        exit()
    for nx in edge[x]:
        if seen[nx]:
            continue
        seen[nx] = True

        dfs(nx)
        seen[nx] = False


N,M = map(int,input().split())
edge = [[]*N for _ in range(N)]

for _ in range(M):
    u,v = map(int,input().split())
    u -= 1
    v -= 1
    edge[u].append(v)
    edge[v].append(u)
    
seen = [False]*(N)
cnt = 0
dfs(0)
print(cnt+1)

    
        
    
    

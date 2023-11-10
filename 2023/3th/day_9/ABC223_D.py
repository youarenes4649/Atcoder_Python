import sys
import heapq

N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(M)]
G = [[] * (N + 1)  for _ in range(N)]
indeg = [0] * (N + 1)
for a,b in AB:
    G[a].append(b)
    indeg[b] += 1
    
q = []
for i in range(1,N+1):
    if indeg[i] == 0:
        heapq.heappush(q,i)
ans = []
while len(q) > 0:
    now = heapq.heappop(q)
    ans.append(now)
    for to in G[now]:
        indeg[to] -= 1
        if indeg[to] == 0:
            heapq.heappush(q,to)
            
if len(ans) == N:
    print(*ans)
else:
    print(-1)
            
    
    
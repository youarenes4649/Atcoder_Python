from collections import deque

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

color = [1] * n
a = []
INF = float("INF")
for _ in range(int(input())):
    p, d = map(int, input().split())
    p -= 1
    a.append((p,d))
    que = deque([])
    que.append(p)
    dist = [INF] * n
    dist[p] = 0
    
    while len(que) > 0:
        now = que.popleft()
        
        if dist[now] < d:
            color[now] = 0
        for to in g[now]:
            if dist[to] == INF:
                que.append(to)
                dist[to] = dist[now] + 1
                
for p,d in a:
    que = deque([])
    que.append(p)
    dist = [INF] * n
    dist[p] = 0
    ok = False
    while len(que) > 0:
        now = que.popleft()
        
        if color[now] and dist[now] == d:
            ok = True 
            break
        
        for to in g[now]:
            if dist[to] == INF:
                dist[to] = dist[now] + 1
                que.append(to)
                
    if not ok:
        print('No')
        exit()
        
print('Yes')
print(*color,sep = '')
                
                
        
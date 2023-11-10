import heapq

N, W = map(int, input().split())
INF = 1 << 60

graph = [[] for i in range(N)]
loop = [INF]*N
for i in range(W):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append((y, z))
    if x == y:
        loop[x] = min(loop[x], z)

dists = []
for s in range(N):
    dist = [INF] * N
    dist[s] = 0
    edgelist = []
    edgelist.append([dist[s], s])
    while edgelist:
        cost, f = heapq.heappop(edgelist)
        if dist[f] < cost:
            continue
        for t, nextcost in graph[f]:
            if dist[t] > dist[f] + nextcost:
                dist[t] = dist[f] + nextcost
                heapq.heappush(edgelist, (dist[t], t))
    dists.append(dist)

for s in range(N):
    ans = loop[s]
    for t in range(N):
        if s == t:
            continue
        ans = min(ans, dists[s][t] + dists[t][s])
    if ans > (1 << 59):
        print(-1)
    else:
        print(ans)

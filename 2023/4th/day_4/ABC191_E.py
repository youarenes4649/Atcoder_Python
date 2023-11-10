from collections import defaultdict
from heapq import heappop, heappush


n, m = map(int, input().split())
G = defaultdict(list)
INF = 10**16
loop = [INF]*(n+1)
for _ in range(m):
  a, b, c = map(int, input().split())
  if a == b: #loopの時は別で考える必要がある？
    loop[a] = min(loop[a], c)
  else:
    G[a].append((c, b))

for i in range(1, n+1):
  h = []
  dist = [INF]*(n+1)
  for c, dest in G[i]:
    heappush(h, (c, dest))
    dist[dest] = min(c, dist[dest])

  while h:
    d, pos = heappop(h)
    if d != dist[pos]: #今見るノードの距離より次が長ければx
      continue
    for d_, dest in G[pos]:
      if d + d_ < dist[dest]:
        dist[dest] = d + d_
        heappush(h, (d + d_, dest))

  if loop[i] != INF:
    dist[i] = min(dist[i], loop[i])

  print(dist[i] if dist[i] != INF else -1)

以下のコードを説明してください
import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import deque

def main():
    def bfs(q):
        que = deque([])
        que.append(q)
        dist = [-1] * (N)
        dist[q] = 0
        while len(que) > 0:
            now = que.popleft()
            for to in edge[now]:
                if dist[to] == -1:
                    dist[to] = dist[now] + 1
                    que.append(to)
        return dist
    
    N = ii()
    edge = [[] * N for _ in range(N)]
    for _ in range(N-1):
        a,b = mi()
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
        
    dist1 = bfs(0)
    second = 0
    score = 0
    for i in range(N):
        if score < dist1[i]:
            score = dist1[i]
            second = i
            
    dist2 = bfs(second)
    print(max(dist2) + 1)
     
    
if __name__ == '__main__':
    main()
    

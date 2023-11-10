import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353


def solve():
    def bfs(i,j):#takahashi aoki
        dist = [[-1] * N for _ in range(N)]
        que = deque()
        dist[i][j] = 0
        que.append([i,j]) #２人の遷移状態を記録
        
        while len(que) > 0:
            v = que.popleft()
            for next_v1 in edge[v[0]]:
                for next_v2 in edge[v[1]]:
                    if dist[next_v1][next_v2] != -1 or C[next_v1] == C[next_v2]:
                        continue
                    dist[next_v1][next_v2] = dist[v[0]][v[1]] + 1
                    que.append([next_v1,next_v2])
            
        return dist
        
    N,M = mi()
    C = li()
    edge = [[] * N for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        edge[u].append(v)
        edge[v].append(u)   
    dist = bfs(0,N-1)
    print(dist[N-1][0])
    
        
T = ii()
for _ in range(T):
    solve()

        
    
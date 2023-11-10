import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

def main():
    from collections import deque
    def bfs(x):
        que = deque([])
        que.append(x)
        seen[x] = True
        while len(que) > 0:
            now = que.popleft()
            for nx in edge[now]:
                if seen[nx]:
                    continue
                seen[nx] = True
                dist[nx] = dist[now] + 1
                que.append(nx)

                
            
            
    N,M = mi()
    edge = [[] * N for _ in range(N)]
    for _ in range(M):
        a,b = mi()
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
    
    for i in range(N):
        dist = [0] * N
        seen = [False] * N
        
        bfs(i)
        print(dist.count(2))
        
if __name__ == '__main__':
    main()
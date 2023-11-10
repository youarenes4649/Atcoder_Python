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
    N,M = mi()
    edge = [[] * N for _ in range(N)]
    for _ in range(M):
        u,v = mi()
        u -= 1
        v -= 1
        edge[u].append(v)
        

    ans = 0
    for i in range(N): #O(NM)
        que = deque([])
        dist = [-1] * N
        
        que.append(i)
        dist[i] = 0
        
        while len(que) > 0:
            x = que.popleft()
            for nx in edge[x]:
                if dist[nx] != -1:
                    continue
                dist[nx] = dist[x] + 1
                ans += 1 #到達かのであれば+
                que.append(nx)
                
                
    print(ans - M)
                
        
if __name__ == '__main__':
    main()
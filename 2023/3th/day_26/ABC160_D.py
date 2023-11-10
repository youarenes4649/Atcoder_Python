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
    N,X,Y = mi()
    edge = [[] * N for _ in range(N)]
    for i in range(N-1):
        edge[i].append(i + 1)
        edge[i + 1].append(i)
    edge[X - 1].append(Y - 1)
    edge[Y - 1].append(X - 1)
        
    ans = [0] * (N)
    for i in range(N):
        que = deque([])
        que.append(i)
        dist = [-1] * (N)
        dist[i] = 0
        
        while len(que) > 0:
            now = que.popleft()
            
            for to in edge[now]:
                if dist[to] != -1:
                    continue
                dist[to] = dist[now] + 1
                que.append(to)
        for d in dist:
            ans[d] += 1
    for i in range(1,N):
        print(ans[i] // 2)
if __name__ == '__main__':
    main()
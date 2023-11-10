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
    for i in range(N):
        que = deque([])
        que.append(i)
        dist = [-1] * N
        dist[i] = 0
        while len(que) > 0:
            now = que.popleft()
            for to in edge[now]:
                if dist[to] != -1:
                    continue
                dist[to] = dist[now] + 1
                ans += 1 #行ける辺は全て追加
                que.append(to)
                
    print(ans - M)
if __name__ == '__main__':
    main()
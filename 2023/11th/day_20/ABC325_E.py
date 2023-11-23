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
    N,A,B,C = mi()
    D = []
    for _ in range(N):
        d = li()
        D.append(d)

# 最初から社用車→電車 bottle neck 部分
# 電車のみ、社用車のみ
# ここら辺の解法を忘れてしまっている気がする
    def dijk(i,x,y):
        que = deque([])
        que.append([0,i])
        dist = [inf for _ in range(N)]
        dist[i] = 0
        while len(que) > 0:
            c,now = que.popleft()

            for nex,nc in enumerate(D[now]):
                d = c + nc*x + y
                if d < dist[nex]:
                    dist[nex] = d
                    que.append([d,nex])

        return dist

    car = dijk(0,A,0)
    train = dijk(N-1,B,C)
    ans = inf
    for i in range(N):
        ans = min(ans,car[i]+train[i])

    print(ans)

if __name__ == '__main__':
    main()
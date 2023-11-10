import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import deque,defaultdict
#順番が一意に決まるということは閉路がない  ということよりトポロジカルソートで順番を特定できる
def main():
    N,M = mi()
    indeg = [0] * (N)
    edge = [[] * N for _ in range(N)]
    for _ in range(M):
        x,y = mi()
        x -= 1
        y -= 1
        indeg[y] += 1
        edge[x].append(y)
    
    que = deque()
    for i in range(N):
        if indeg[i] == 0:
            que.append(i)
    ans = []
    while len(que) > 0:
        if len(que) >= 2:
            print('No')
            exit()
        now = que.popleft()
        ans.append(now+1)
        for to in edge[now]:
            indeg[to] -= 1
            if indeg[to] == 0:
                que.append(to)
    
    change = [0] * N

    for i,a in enumerate(ans):
        change[a-1] = i + 1
        
    print('Yes')
    print(*change)
  
if __name__ == '__main__':
    main()
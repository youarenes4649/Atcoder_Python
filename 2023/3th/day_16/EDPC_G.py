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
    indeg = [0] * N
    for _ in range(M):
        x,y = mi()
        x -= 1
        y -= 1
        edge[x].append(y)
        indeg[y] += 1
        
    que = deque([])
    for i in range(N):
        if indeg[i] == 0:
            que.append(i)#最初の候補
    ans = 0
    while len(que) > 0:
        next_ls = []
        for now in que:
            for to in edge[now]:
                indeg[to] -= 1
                if indeg[to] == 0:
                    next_ls.append(to)
        que = next_ls.copy()
        ans += 1
        
    print(ans-1)
        
                
    
    
    
    
if __name__ == '__main__':
    main()
    
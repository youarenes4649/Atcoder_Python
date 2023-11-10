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
        l,r,d = mi()
        l -= 1
        r -= 1
        edge[l].append((d,r))
        edge[r].append((-d,l))
        
    for i in range(N):
        edge[i].sort()
        #print(edge[i])
        
    dist = [-1] * N
    seen = [False] * N
    for i in range(N):
        if seen[i]:
            continue
        
        que = deque([])
        que.append(i)
        dist[i] = 0
        seen[i] = True
        while len(que) > 0 :
            now = que.popleft()
            for cost,to in edge[now]:
                if seen[to]:
                    if dist[to] != dist[now] + cost:
                        print('No')
                        exit()
                    continue
                
                dist[to] = dist[now] + cost
                seen[to] = True
                que.append(to)
                
    print('Yes')

if __name__ == '__main__':
    main()
    
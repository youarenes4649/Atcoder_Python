import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
import heapq

def main():
    def dijkstra(s):
        que = [(0,s,-1)]
        dist = [10 ** 20] * N
        while len(que) > 0:
            nc,now,pre= heapq.heappop(que)
            #既に訪れていたら
            for to,cost in edge[now]:
                if dist[to] != 10 ** 20:
                    continue
                if dist[to] > nc + cost:
                    dist[to] = nc + cost
                    heapq.heappush(que,(dist[to],to,now))
                    
        return dist
        
        
    N,M = mi()
    edge = [[] * N for _ in range(N)]
    for i in range(M):
        a,b,c = mi()
        a -= 1
        b -= 1
        edge[a].append((b,c))
    
    for i in range(N):
        dist = dijkstra(i)
        if dist[i] == 10 ** 20:
            print(-1)
        else:
            print(dist[i])
if __name__ == '__main__':
    main()
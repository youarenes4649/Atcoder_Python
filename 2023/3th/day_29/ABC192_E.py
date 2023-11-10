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
    N,M,X,Y = mi()
    X -= 1
    Y -= 1
    train = [[] * N for _ in range(N)]
    for i in range(M):
        A,B,T,K = mi()
        A -= 1
        B -= 1
        train[A].append((B,T,K))
        train[B].append((A,T,K))
    
    dist = [10 ** 20] * N
    dist[X] = 0
    que = [(0,X)]
    while len(que) > 0:
        nowtime,now = heapq.heappop(que)
        if nowtime > dist[now]:
            continue
        
        for to,time,k in train[now]:  
            #初項:出発時間　,２項:乗車時間
            nexttime = ((nowtime + k - 1) // k) * k + time
            
            if dist[to] > nexttime :
                dist[to] = nexttime
                que.append((nexttime,to))
                
    print(dist[Y] if not dist[Y] == 10 ** 20 else -1 )
if __name__ == '__main__':
    main()
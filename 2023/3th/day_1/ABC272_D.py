import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
from collections import deque
def main():
    N,M = mi()
    dist = [[-1] * N for _ in range(N)]
    dist[0][0] = 0
    cand = []
    for i in range(10 ** 3 + 1):
        for j in range(10 ** 3 + 1):
            if i ** 2 + j ** 2 == M:
                cand.append((i,j))
                cand.append((-i,j))
                cand.append((i,-j))
                cand.append((-i,-j))
        
    que = deque([])
    que.append((0,0))
    while len(que) > 0 :
        x,y = que.popleft()
        
        for dx,dy in cand:
            next_x = x + dx
            next_y = y + dy
            if 0 <= next_x < N and 0 <= next_y < N:
                if dist[next_x][next_y] == -1:
                    dist[next_x][next_y] = dist[x][y] + 1
                    que.append((next_x,next_y))
                    
    for i in range(N):
        print(*dist[i])
      
if __name__ == '__main__':
    main()
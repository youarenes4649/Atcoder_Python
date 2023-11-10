import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
night = ((1,2),(1,-2),(-1,2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1))
from collections import deque
def main():
    N = 50
    edge = [[10 ** 20] * N for _ in range(N)]
    que = deque([])
    que.append([0,0])
    edge[0][0] = 0
    ans = 0
    while len(que) > 0:
        x,y = que.popleft()
        
        for dx,dy in night:
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < N and 0 <= y < N:
                if edge[nx][ny] > edge[x][y] + 1 :
                    edge[nx][ny] = edge[x][y] + 1
                    que.append([nx,ny])
                    
                    if edge[nx][ny] == 21:
                        ans += 1
    print(ans)
                    
                
                        
    
if __name__ == '__main__':
    main()
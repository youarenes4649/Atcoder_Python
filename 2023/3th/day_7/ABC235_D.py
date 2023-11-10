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
    a,N = mi()
    M = 1
    while M <= N:
        M *= 10
        
    que = deque([])
    que.append(1)
    dist = [-1] * (M + 1)
    dist[1] = 0
    while len(que) > 0:
        n = que.popleft()
        if n > M:
            continue
    
        n1 = n * a
        if n1 < M and dist[n1] == -1:
            dist[n1] = dist[n] + 1
            que.append(n1)
            
        if n >= 10 and  n%10 != 0 and dist[int(str(n)[-1] + str(n)[:-1])] == -1:
            n2 = int(str(n)[-1] + str(n)[:-1])
            if n2 < M:
                dist[n2] = dist[n] + 1
                que.append(n2)
            
    print(dist[N])
if __name__ == '__main__':
    main()
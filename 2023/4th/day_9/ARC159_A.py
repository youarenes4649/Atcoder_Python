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
    def solve(s,t):
        que = deque([])
        dist = [0] * N
        seen = [False] * N
        que.append([0,s])
        
        while len(que) > 0:
            d,now = que.popleft()
 
            for i,to in enumerate(A[now]):
                if to == 0:
                    continue
                if seen[i]:
                    continue
                seen[i] = True
                dist[i] = d + 1
                que.append([d+1,i])
        return dist[t] if dist[t] != 0 else -1

    N,K = mi()
    A = []
    for _ in range(N):
        a = li()
        A.append(a)
    Q = ii()
    for _ in range(Q):
        s,t = mi()
        s -= 1
        t -= 1
        s = s - N * (s // N)
        t = t - N * (t // N)
        print(solve(s,t))
if __name__ == '__main__':
    main()
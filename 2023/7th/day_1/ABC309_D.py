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
    n1,n2,M = mi()
    edge = [[] for _ in range(n1+n2)]
    
    for _ in range(M):
        a,b = mi()
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
        
    dist1 = [-1] * n1
    que1 = deque([])
    dist1[0] = 0
    que1.append(0)
    
    while len(que1) > 0:
        now = que1.popleft()
        for to in edge[now]:
            if dist1[to] == -1:
                dist1[to] = dist1[now] + 1
                que1.append(to)

    dist2 = [-1] * n2
    que2 = deque([])
    dist2[n2-1] = 0
    que2.append(n2-1)
    while len(que2) > 0:
        now = que2.popleft()
        for to in edge[now + n1]:
            to -= n1
            if dist2[to] == -1:
                dist2[to] = dist2[now] + 1
                que2.append(to)

    print(max(dist1) + max(dist2) + 1)
if __name__ == '__main__':
    main()
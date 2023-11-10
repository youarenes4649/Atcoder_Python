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
    r, c = mi()
    inf = float('inf')
    dis = [inf] * (r * c)
    dis[0] = 0
    a = []
    b = []
    for i in range(r):
        a.append(li())
    for i in range(r - 1):
        b.append(li())
    pq = []
    pq.append((0, 0))
    while pq:
        d, p = heapq.heappop(pq)
        x = p // c
        y = p % c
        if d != dis[x * c + y]: continue
        if y + 1 < c:
            if dis[x * c + y + 1] > d + a[x][y]:
                dis[x * c + y + 1] = d + a[x][y]
                heapq.heappush(pq, (dis[x * c + y + 1], x * c + y + 1))
        if y > 0:
            if dis[x * c + y - 1] > d + a[x][y - 1]:
                dis[x * c + y - 1] = d + a[x][y - 1]
                heapq.heappush(pq, (dis[x * c + y - 1], x * c + y - 1))
        if x + 1 < r:
            if dis[(x + 1) * c + y] > d + b[x][y]:
                dis[(x + 1) * c + y] = d + b[x][y]
                heapq.heappush(pq, (dis[(x + 1) * c + y], (x + 1) * c + y))
        for i in range(1, x + 1):
            if dis[(x - i) * c + y] > d + i + 1:
                dis[(x - i) * c + y] = d + i + 1
                heapq.heappush(pq, (dis[(x - i) * c + y], (x - i) * c + y))
    print(dis[r * c - 1])
      
if __name__ == '__main__':
    main()
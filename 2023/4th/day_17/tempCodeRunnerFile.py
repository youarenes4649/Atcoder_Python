import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from collections import defaultdict
def main():
    N = ii()
    Q = ii()
    boxes = defaultdict(list)
    number = defaultdict(list)
    for _ in range(Q):
        query = li()
        if query[0] == 1:
            i,j = query[1:]
            boxes[j].append(i)
            number[i].append(j)
        if query[0] == 2:
            i = query[1]
            boxes[i].sort()
            print(*boxes[i])
        if query[0] == 3:
            i = query[1]
            number[i].sort()
            print(*number[i])
if __name__ == '__main__':
    main()
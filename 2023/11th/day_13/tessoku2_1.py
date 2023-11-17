import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
from itertools import accumulate
def main():
    N,Q = mi()
    A = li()
    A_sum = [0] + list(accumulate(A))
    for _ in range(Q):
        l,r = mi()
        print(A_sum[r] - A_sum[l-1])


if __name__ == '__main__':
    main()
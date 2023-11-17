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
    def solve(l,r):
        if A_sum[r] - A_sum[l-1] >0:
            print('win')
        elif A_sum[r] - A_sum[l-1] == 0:
            print('draw')
        else:
            print('lose')

    N = ii()
    A = li()
    for i in range(N):
        if A[i] == 0:
            A[i] = -1
    
    A_sum = [0] + list(accumulate(A))

    Q = ii()
    for _ in range(Q):
        l,r = mi()
        solve(l,r)


if __name__ == '__main__':
    main()
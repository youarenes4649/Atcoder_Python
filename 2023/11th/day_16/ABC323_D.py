import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
import bisect
from itertools import accumulate
def main():
    N,M,P = mi()
    A = li()
    B = li()
    A.sort()
    B.sort()
    A_cum = [0] + list(accumulate(A))

    ans = 0
    for i in range(M):
        b = B[i]
        can_eat = P - b
        can_eat_a = bisect.bisect_right(A,can_eat)
        tmp_total = b * can_eat_a + A_cum[can_eat_a] + P * (N - can_eat_a)
        ans += tmp_total

    print(ans)



    


if __name__ == '__main__':
    main()
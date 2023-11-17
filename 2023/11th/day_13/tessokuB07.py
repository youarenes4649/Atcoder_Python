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
    T = ii()
    N = ii()

    Time = [0] * (2*T + 1)
    for _ in range(N):
        l,r = mi()
        l *= 2
        r *= 2
        Time[l] += 1
        Time[r] -= 1

    attendance = list(accumulate(Time))
    for h in range(T):
        print(attendance[2 * h + 1])


if __name__ == '__main__':
    main()
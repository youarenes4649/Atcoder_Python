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
    D = ii()
    N = ii()
    attendance = [0] * (D+1)
    for i in range(N):
        l,r = mi()
        l -= 1
        r -= 1
        attendance[l] += 1
        attendance[r+1] -= 1

    attendance_sum = list(accumulate(attendance))
    for i in range(D):
        print(attendance_sum[i])
if __name__ == '__main__':
    main()
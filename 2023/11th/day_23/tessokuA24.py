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
def main():
    N = ii()
    A = li()

    dp = [0] * N # dp[i] i番目まで見た時の最長
    L = [inf] * N

    dp[0] = 1
    L[0] = A[0]

    for i in range(1,N):
        L_idx = bisect.bisect_left(L,A[i])
        L[L_idx] = A[i]
        dp[i] = L_idx + 1

    print(dp[-1])
    



if __name__ == '__main__':
    main()
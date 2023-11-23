import sys
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 63 - 1
mod = 998244353
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
def main():
    N,M = mi()
    A = []
    for _ in range(M):
        a = li()
        A.append(a)

    dp = [[inf] * (1 << N) for _ in range(M+1)]
    dp[0][0] = 0

    for i in range(1,M+1):
        for S in range(1 << N):
            dp[i][S] = min(dp[i][S],dp[i-1][S])#何も取らないとき
            new_S = S
            for j in range(N):
                if A[i-1][j] == 1:
                    new_S |= (1 << j)

            dp[i][new_S] = min(dp[i][new_S],dp[i-1][S]+1)

    if dp[M][(1<<N)-1] > M:
        print(-1)
    else:
        print(dp[M][(1<<N)-1])



if __name__ == '__main__':
    main()
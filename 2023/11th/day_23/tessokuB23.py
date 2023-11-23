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
    N = ii()
    X = []
    Y = []

    for _ in range(N):
        x,y = mi()
        X.append(x)
        Y.append(y)

    dp = [[inf] * (N) for _ in range(1 << N)]
    dp[0][0] = 0

    for S in range(1<<N):
        for fr in range(N):
            if dp[S][fr] == inf: #もしfrが集合に含まれていなかったらcontinue
                continue
            for to in range(N):
                if S & (1<<to) == 0:
                    dist = (X[fr] - X[to])**2 + (Y[fr] - Y[to])**2
                    dist = dist**0.5

                    dp[S|(1<<to)][to] = min(dp[S|(1<<to)][to],dp[S][fr]+dist)

    print(dp[(1<<N)-1][0])

if __name__ == '__main__':
    main()
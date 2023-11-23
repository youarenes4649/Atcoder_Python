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
    N,W = mi()
    Weight = []
    Value = []
    for _ in range(N):
        w,v = mi()
        Weight.append(w)
        Value.append(v)

    dp = [[-inf] * (W + 1) for _ in range(N+1)]
    
    for i in range(W+1):
        dp[0][i] = 0

    for i in range(1,N):
        for j in range(W+1):
            if j - Weight[i] >= 0:
                dp[i][j] = max(dp[i][j],dp[i-1][j-Weight[i]]+Value[i-1])

            else:
                dp[i][j] = dp[i-1][j]
    print(max(dp[N]))

if __name__ == '__main__':
    main()
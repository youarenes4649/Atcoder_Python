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
    h = li()

    dp = [inf] * N
    dp[0] = 0
    for i in range(1,N):
        if i == 1:
            dp[i] = min(dp[i],dp[i-1] + abs(h[i] - h[i-1]))

        else:
            dp[i] = min(dp[i],dp[i-1] + abs(h[i] - h[i-1]),dp[i-2] + abs(h[i] - h[i-2]))


    print(dp[-1])


if __name__ == '__main__':
    main()
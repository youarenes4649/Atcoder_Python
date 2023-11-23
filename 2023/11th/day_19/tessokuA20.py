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
    S = list(map(str,input()))
    T = list(map(str,input()))

    dp = [[0] * (len(T)+1) for _ in range(len(S)+1)]

    for i in range(1,len(S)+1):
        for j in range(1,len(T)+1):
            if S[i-1] == T[j-1]:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]+1)
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

    print(dp[len(S)][len(T)])

if __name__ == '__main__':
    main()
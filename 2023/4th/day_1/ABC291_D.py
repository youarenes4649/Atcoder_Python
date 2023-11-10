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
    A = []
    B = []
    for _ in range(N):
        a,b = mi()
        A.append(a)
        B.append(b)
    dp = [[0] * 2 for _ in range(N)]
    dp[0][0] = 1
    dp[0][1] = 1
    for i in range(1,N):
        if A[i-1] != A[i]:
            dp[i][0] += dp[i-1][0]
            dp[i][0] %= mod
        if A[i-1] != B[i]:
            dp[i][1] += dp[i-1][0]
            dp[i][1] %= mod 
        if B[i-1] != A[i]:
            dp[i][0] += dp[i-1][1]
            dp[i][0] %= mod
        if B[i-1] != B[i]:
            dp[i][1] += dp[i-1][1]
            dp[i][1] %= mod 
            
    print(sum(dp[-1])%mod)
                      
if __name__ == '__main__':
    main()
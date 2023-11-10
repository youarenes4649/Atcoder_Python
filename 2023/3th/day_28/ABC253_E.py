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
    N,M,K = mi()
    dp = [[0] * (M + 3) for _ in range(N)]
    #初項は１〜Mどれでもok
    for i in range(1,M+1):
        dp[0][i] = 1
        
    for i in range(1,N):
        cum = dp[i-1]
        for j in range(1,M+3):
            cum[j] += cum[j-1] 
            cum[j] %= mod
        
        #l ~ r の結果が欲しい時 累積和ではcum[r] - cum[l - 1]で得ることができる
        for j in range(1,M+1):
            dp[i][j] = (cum[M] - cum[min(M,j+K-1)]) + (cum[max(0,j-K)] - cum[0])
            dp[i][j] %= mod
            
    print(sum(dp[-1]) % mod)
            
if __name__ == '__main__':
    main()
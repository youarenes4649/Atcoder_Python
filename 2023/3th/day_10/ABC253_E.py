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
    if K == 0:
        print(pow(M,N,mod))
        exit()
    dp = [[0] * (M + 3) for _ in range(N)]
    
    for j in range(1,M+1):
        dp[0][j] = 1
        
    for i in range(1,N):
        accum = dp[i-1]
        for j in range(1,M + 3):
            accum[j] += accum[j-1]
            accum[j] %= mod
            
        for j in range(1,M+1):
            dp[i][j] = (accum[M] - accum[0]) - (accum[min(M+2,j+K-1)] - accum[max(0,j-K)])
            dp[i][j] %= mod
            
    print(sum(dp[-1])%mod)
        
    
    
    
    
    
if __name__ == '__main__':
    main()
N,M,K=map(int,input().split())
mod=998244353

dp=[[0]*(M+1) for _  in range(N+1)]

for i in range(N+1):
    for j in range(1,M+1):
        dp[i][j+K]=dp[i-1][j]
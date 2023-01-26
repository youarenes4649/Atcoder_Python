N,M,K=map(int,input().split())
mod=998244353

dp=[[0]*(K+1) for _ in range(N+1)]

dp[0][0]=1

for i in range(N):

    for j in range(K+1):

        for k in range(1,M+1):
            if j+k<=K:
                dp[i+1][j+k]+=dp[i][j]
                dp[i+1][j+k]%=mod

ans=0
for i in range(1,K+1):
    ans+=dp[N][i] 
print(sum(dp[N])%mod)




N,M,K,S,T,X=map(int,input().split())
mod=998244353

S-=1
T-=1
X-=1

edge=[]

for i in range(M):
    U,V=map(int,input().split())
    U-=1
    V-=1
    edge.append((U,V))
#dp[i][j][x] i:試行回数max:K j 頂点　x mod2 
dp=[[[0]* N for i in range(K+1)] for x in range(2)]

dp[0][0][S]=1# 途中で頂点Sを通った回数 Sを通ってなかったら edgeで全部回ってるけど中身は０になる
for i in range(K):
    for U,V in edge:
        for x in range(2):
            dp[x][i+1][V]+=dp[x^(V==X)][i][U]

            if dp[x][i+1][V]>=mod:
                dp[x][i+1][V]-=mod

            dp[x][i + 1][U] += dp[x ^ (U == X)][i][V]
            if dp[x][i + 1][U] >= mod:
                dp[x][i + 1][U] -= mod
print(dp[0][K][T])




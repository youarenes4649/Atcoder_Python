N,M=map(int,input().split())
X=[0]+list(map(int,input().split()))

C=[0]*(N+1)
Y=[0]*(N+1)
for i in range(M):
    c,y=map(int,input().split())
    C[i]=c
    Y[c]=y
 
dp=[[-1]*(N+1) for _ in range(N+1)]
dp[0][0]=0#dp[i][j]i回目までコイントスをやって現在のカウンタの数値がjである

for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i][j]=max(dp[i][j],dp[i-1][j-1]+X[i]+Y[j])

    dp[i][0]=0
    for j in range(i):
        dp[i][0]=max(dp[i-1][j],dp[i][0])


ans=0
for n in range(N+1):
    ans=max(ans,dp[N][n])

print(ans)



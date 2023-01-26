N,K,D=map(int,input().split())
A=list(map(int,input().split()))
#dp[i][j] i番目まででk個とったときの総和
ans=set()

dp = [[[-1] * D for k in range(N+1)] for j in range(N+1)]
dp[0][0][0] = 0
for j in range(N): # 配列A の選択範囲（先頭から）
    for k in range(K+1): #選択する個数
        for l in range(D): #計算して得られた余り
            if dp[j][k][l]==-1:
                continue
            dp[j+1][k][l]=max(dp[j+1][k][l],dp[j][k][l])#選ばない時の最大値
            if k!=K:
                dp[j+1][k+1][(l+A[j])%D]=max(dp[j+1][k+1][(l+A[j])%D],dp[j][k][l]+A[j])
            
print(dp[N][K][0])

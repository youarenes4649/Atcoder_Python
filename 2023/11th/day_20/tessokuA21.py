N = int(input())
P, A = zip([0,0], *[map(int, input().split()) for _ in range(N)])
#0で埋めることで1,Nで扱えるようにしている
dp = [[0]*(N+1) for _ in range(N+1)]
for l in range(1,N):        # 1,2,...,N-1
    for r in range(N,l,-1): # N,N-1,...,l+1
        # remove left end
        dp[l+1][r] = max(dp[l+1][r],dp[l][r] + (A[l] if l <= P[l] <= r else 0))
        # remove right end
        dp[l][r-1] = max(dp[l][r-1], dp[l][r] + (A[r] if l <= P[r] <= r else 0))

ans = max(dp[i][i] for i in range(1,N+1))
print(ans)
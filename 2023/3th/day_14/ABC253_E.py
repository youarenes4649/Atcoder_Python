N, M, K = map(int, input().split())
MOD = 998244353
if K == 0:
    ans = 1
    for _ in range(N):
        ans *= M
        ans %= MOD
    print(ans)
    exit()

dp = [[0]*(M+1) for _ in range(N)]
cs = [0]*(M+1)
for j in range(1, M+1):
    dp[0][j] = 1
    cs[j] = cs[j-1]+dp[0][j]

for i in range(1, N):
    for j in range(1, M+1):
        if j+K-1 < M:
            dp[i][j] = (dp[i][j] + cs[M]-cs[j+K-1])%MOD
        if j-K >= 1:
            dp[i][j] = (dp[i][j] + cs[j-K])%MOD
    for j in range(1, M+1):
        cs[j] = (cs[j-1]+dp[i][j])%MOD
ans = 0
for j in range(1, M+1):
    ans += dp[N-1][j]
    ans %= MOD
print(ans)
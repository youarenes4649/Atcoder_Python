s = [int(c) for c in input()]
L = len(s)
dp = [[0,0] for _ in range(L+1)]
'''
dp[i][j]:左からi桁まで決めたときの個数
j=0で一致、j=1で未満確定
'''
dp[0][0] = 1
mod = 10**9 +7
for i in range(L):
    c = s[i]
    # xorを0とするとき（aもbもどちらも0）
    if c == 0:
        dp[i+1][0] += dp[i][0] % mod
        dp[i+1][1] += dp[i][1] % mod
        
    else:
        dp[i+1][1] += dp[i][0] % mod
        dp[i+1][1] += dp[i][1] % mod
        
    if c == 0:
        dp[i+1][1] += dp[i][1] * 2
        dp[i+1][1] %= mod
        
    else:
        dp[i+1][0] += dp[i][0] * 2
        dp[i+1][0] %= mod
        dp[i+1][1] += dp[i][1] * 2 
        dp[i+1][1] %= mod
        
print((dp[L][0] + dp[L][1]) % mod)
        
        
        
        
    
N, M = map(int, input().split())
A = []
for i in range(M):
    A.append(list(map(int, input().split())))
dp = [[1 << 60] * (1 << N) for i in range(M+1)]
dp[0][0] = 0
for i in range(1,M+1):
    for S in range(1<<N):#N個までどれをとるか取らないかの２択
        dp[i][S]=min(dp[i][S],dp[i-1][S])#ticketをとらないとき
        T=S
        for k in range(N):#Nこの中からk番目をとりたい
            if A[i-1][k]==1:#i番目のチケットのうちk個めを無料にできるとき
                T |= 1 << k #kを二進表記に直すことで論理和をとる

        dp[i][T]=min(dp[i][T],dp[i-1][S]+1)

if dp[M][(1 << N) - 1] <= M:
    print(dp[M][(1 << N) - 1])
else:
    print(-1)
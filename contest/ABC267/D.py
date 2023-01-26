N, M = map(int, input().split()) 
A = list(map(int, input().split()))

dp = []
for i in range(N + 1):
  list = [-10 ** 12] * (M + 1)
  dp.append(list)

for i in range(N + 1):
  dp[i][0] = 0


for i in range(1, N + 1):
  for j in range(1, M + 1):
    if j <= i:
      dp[i][j] = max(dp[i - 1][j - 1] + j * A[i - 1], dp[i - 1][j])
    

print(dp[N][M])
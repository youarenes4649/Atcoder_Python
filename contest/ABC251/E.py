N=int(input())
count=[0]*(N)

A=list(map(int,input().split()))

dp1=[[10**20]*2 for _ in range(N)]#１番目を与える場合　
dp2=[[10**20]*2 for _ in range(N)]#１番目を与えない場合　

dp1[0][1]=A[0]
for i in range(1,N):
    dp1[i][0]=dp1[i-1][1]
    dp1[i][1]=min(dp1[i-1][0]+A[i],dp1[i-1][1]+A[i])

dp2[0][0]=0
for i in range(1,N):
    dp2[i][0]=dp2[i-1][1]
    dp2[i][1]=min(dp2[i-1][0]+A[i],dp2[i-1][1]+A[i])

ans=min(dp2[N-1][1],min(dp1[N-1][0],dp1[N-1][1]))

print(ans)




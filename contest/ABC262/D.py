from cv2 import mean


N=int(input())
a=list(map(int,input().split()))
mod=998244353
dp=[[0]*(10**9//N+1) for _ in range(N+1)]

dp[0][0]=1

for i in range(1,N+1):
    for j in range(10**9//N+1):
        int_=((i-1)*j+a[i-1])/(i)
        if isinstance(int_,int) and int_>=0:
            dp[i][int_]+=dp[i-1][j]
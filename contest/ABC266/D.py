N=int(input())
Tmax=10**5
X=[0]*(Tmax+1)
A=[0]*(Tmax+1)
for i in range(N):
    t,x,a=map(int,input().split())
    X[t]=x
    A[t]=a

dp=[[0]*(Tmax+1) for _ in range(5)]#dp[i][j] i秒めにj番目にいる時の最大スコア


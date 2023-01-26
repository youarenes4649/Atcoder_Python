#dp 復元
N,S=map(int,input().split())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

dp=[[False]*(S+1) for _ in range(N+1)]#配るdpならS+1まででok
dp[0][0]=True

for i in range(N):
    for s in range(S+1):
        if not dp[i][s]:
            continue
        if s+A[i]<=S:#配る系なら上限Sで固定できる
            dp[i+1][s+A[i]]=True

        if s+B[i]<=S:
            dp[i+1][s+B[i]]=True


if dp[N][S]:
    print('Yes')
    ans=''
    for i in range(N-1,-1,-1):
        if A[i]<=S and dp[i][S-A[i]]:
            ans+='H'
            S-=A[i]
        else:
            ans+='T'
            S-=B[i]

    print(ans[::-1])

    

else:
    print('No')

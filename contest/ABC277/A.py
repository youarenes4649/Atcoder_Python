N,X=map(int,input().split())
P=list(map(int,input().split()))
ans=0
for i in range(N):
    if P[i]==X:
        ans=i+1


print(ans)

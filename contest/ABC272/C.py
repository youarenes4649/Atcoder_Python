N=int(input())
A=list(map(int,input().split()))
A.sort()
check=[False]*(N)
cnt=0
for i in range(N):
    if A[i]%2==0:
        check[i]=True
        cnt+=1



ans=0
cnt=0
ans1=0
for i in range(N-1,-1,-1):
    if check[i]==True:
        cnt+=1
        if cnt==2:
            ans1=ans+A[i]
        ans+=A[i]
if N==1:
    if A[0]%2==0:
        print(A[0])
        exit()

    else:
        print(-1)
        exit()

if N==2:
    if cnt==1:
        print(-1)
        exit()
    else:
        print(sum(A))
        exit()

ans=0
cnt=0
ans2=0
for i in range(N-1,-1,-1):
    if check[i]==False:
        cnt+=1
        if cnt==2:
            ans2=ans+A[i]
        ans+=A[i]

print(max(ans1,ans2))



        




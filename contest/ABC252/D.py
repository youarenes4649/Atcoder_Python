N=int(input())
A=list(map(int,input().split()))

cnt=[0]*(2*10**5+1)
for i in range(N):
    cnt[A[i]]+=1

max_A=max(A)

for i in range(1,2*10**5+1):
    cnt[i]+=cnt[i-1]

ans=0


for j in range(N):
        a_j=A[j]

        ans+=cnt[A[j]-1]*(N-cnt[A[j]])


print(ans)

N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
ans=0
for i in range(N):
    if ans<A[i]:
        ans=A[i]

count=[]
for i in range(N):
    if A[i]==ans:
        count.append(i+1)


for a in count:
    if a in B:
        print('Yes')
        exit()


print('No')



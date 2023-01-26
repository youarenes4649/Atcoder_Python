
N,X,Y=map(int,input().split())
ans=0
rls=[0]*(N+1)
bls=[0]*(N+1)
rls[N]=1
def dfs(n,r,b):

    if n==1:
        return 
    

    b[n]+=r[n]*X
    b[n-1]+=b[n]*Y
    r[n-1]+=r[n]+b[n]
    dfs(n-1,r,b)
dfs(N,rls,bls)
print(bls[1])
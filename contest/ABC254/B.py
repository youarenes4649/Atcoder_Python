N=int(input())
ans=[[1]*N for _ in range(N)]
for i in range(N):
    
    for j in range(i):
        if i==j or j==0:
            ans[i][j]=1

        else:
            ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
for i in range(N):
    print(*ans[i][:i+1])
            

        

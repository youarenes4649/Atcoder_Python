N,M=map(int,input().split())
K=[]
X=[]
for m in range(M):
    lis=list(map(int,input().split()))
    K.append(lis[0])
    X.append(lis[1:])

ok=[[False]*(N) for _ in range(N)]
for i in range(N):
    ok[i][i]=True
for m in range(M):
    for i in range(K[m]-1):
        xi=X[m][i]
        
        for j in range(i+1,K[m]):
            xj=X[m][j]
            ok[xi-1][xj-1]=True
            ok[xj-1][xi-1]=True

for i in range(N):
    for j in range(N):
        if ok[i][j]!=True:
            print('No')
            exit()

print('Yes') 

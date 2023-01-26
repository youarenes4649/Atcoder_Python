N,M,T=map(int,input().split())
A=[0]+list(map(int,input().split()))
from collections  import defaultdict
X=defaultdict(int)
for i in range(M):
    x,y=map(int,input().split())
    X[x]=y

    
i=1
while T>0 and i<N:
    T-=A[i]
    if T<=0:
        break
    i+=1
    if X[i]!= 0:
        T+=X[i]


if i==N:
    print('Yes')

else:
    print('No')
    


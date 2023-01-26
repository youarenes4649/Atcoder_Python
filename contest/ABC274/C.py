N=int(input())
A=list(map(int,input().split()))
ans=[0]*(2*N+2)
from collections import defaultdict
dist=defaultdict(list)
for i in range(1,N+1):
    dist[A[i-1]].append(2*i)
    dist[A[i-1]].append(2*i+1)

ans[1]=0
for n in dist:
    for i in dist[n]:
        ans[i]=ans[n]+1

for a in ans[1:]:
    print(a)




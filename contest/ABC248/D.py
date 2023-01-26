N=int(input())
A=list(map(int,input().split()))
Q=int(input())
from collections import defaultdict

ls=defaultdict(list)
for i in range(N):
    ls[A[i]].append(i+1)

import bisect
ans=[]
for q in range(Q):
    l,r,x=map(int,input().split())

    left=bisect.bisect_left(ls[x],l)
    righ=bisect.bisect_right(ls[x],r)
    ans.append(righ-left)

for a in ans:
    print(a)
    


    

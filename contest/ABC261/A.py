L1,R1,L2,R2=map(int,input().split())
from itertools import accumulate

count=[0]*101

count[L1]+=1
count[L2]+=1
count[R1]-=1
count[R2]-=1
ans=0
count=list(accumulate(count))
for i in range(100):
    if count[i]==2:
        ans+=1

print(ans)

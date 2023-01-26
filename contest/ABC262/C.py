
N=int(input())
a=[0]+list(map(int,input().split()))
from collections import defaultdict
loc=defaultdict(int)

for i in range(1,len(a)):
    loc[i]=a[i]

ans=0
cnt=0
for i in range(1,len(a)):
    if loc[loc[i]]==i:
        ans+=1
        
    if loc[i]==i:
        cnt+=1

ans-=cnt
ans=ans//2+cnt*(cnt-1)//2

print(ans)




N=int(input())
P=list(map(int,input().split()))
from collections import defaultdict
sub=defaultdict(int)
sub2=defaultdict(int)
sub3=defaultdict(int)
for i in range(N):
    sub[(P[i]-i)%N]+=1
for i in range(1,N+1):
    sub2[(P[i-1]-i)%N]+=1
for i in range(2,N+2):
    sub3[(P[i-2]-i)%N]+=1
ans=0
for i in range(-N,N):
    ans=max(sub[i]+sub[i+1]+sub[i+2],ans)
for i in range(-N,N):
    ans=max(sub2[i]+sub2[i+1]+sub2[i+2],ans)
for i in range(-N,N):
    ans=max(sub3[i]+sub3[i+1]+sub3[i+2],ans)

print(ans)


    


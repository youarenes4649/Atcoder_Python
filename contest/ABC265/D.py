N,P,Q,R=map(int,input().split())
A=list(map(int,input().split()))
from itertools import accumulate
A_cum=list(accumulate(A))

#Qを探す
l=0
r=0
sum=0
cand=[]
while l!=N and r!=N:
    if sum+A[r]<=Q:
        sum+=A[r]
        r+=1
        if sum==Q:
            cand.append([l,r])

    else:
        
        sum-=A[l]
        l+=1


one=-1
last=-1
for y,z in cand:
    for l in range(y):
        if A_cum[y-1]-A_cum[l]==P:
            one=l+1
        

    for r in range(z+1,N):
        if A_cum[r]-A_cum[z+1]==R:
        
            last=r


    if one!=-1 and last !=-1:
        print('Yes')
        exit()


print('No')        



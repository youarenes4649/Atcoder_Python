N,M=map(int,input().split())
A=list(map(int,input().split()))
from itertools import accumulate
A_cum=[0]+list(accumulate(A))
r=M
l=0
A_sum=0
for i in range(M):
    A_sum+=A[i]*(i+1)
ans=A_sum
for l in range(N-M):
    A_sum=A_sum-(A_cum[l+M]-A_cum[l])+A[l+M]*M
    ans=max(ans,A_sum)
print(ans)








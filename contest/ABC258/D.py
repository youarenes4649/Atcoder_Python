N,X=map(int,input().split())
from itertools import accumulate
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
A_sum=list(accumulate(A))
B_sum=list(accumulate(B))

ans=10**20
b=10**20
for i in range(N):#istage まで選んだ時の最小値を見ていけばいい
    b=min(b,B[i])
    tmp=A_sum[i]+B_sum[i]+b*(X-(i+1))
    ans=min(ans,tmp)


print(ans)



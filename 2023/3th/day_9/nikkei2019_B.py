from collections import Counter
mod=998244353
n=int(input())
d=list(map(int,input().split()))
q=Counter(d)
if q[0]!=1 or d[0]!=0:
    print(0)
    exit()
ans=1
#勘違いしていた１頂点からの出次数は２だと思っていた
for i in range(1,max(d)+1):
    ans*=pow(q[i-1],q[i],mod)
    ans%=mod
print(ans)
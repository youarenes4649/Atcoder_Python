N=int(input())
S=[]
for i in range(N):
    s=input()
    S.append(s)

from collections import defaultdict
from collections import Counter
count=defaultdict(list)
for s in S:
    for n in range(len(s)):
        count[int(s[n])].append(n)
ans=10**10
for number in count:
    lis=count[int(number)]
    tmp=0
    for l in lis:
        seconds=(lis.count(l)-1)*10+l
        tmp=max(tmp,seconds)

    ans=min(ans,tmp)
print(ans)

 
        




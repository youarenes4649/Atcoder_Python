N=int(input())
S=list(map(str,input()))
W=list(map(int,input().split()))
ans=0
from collections import defaultdict
from itertools import accumulate
SW=defaultdict(list)
ad_max=S.count('1')

for s,w in zip(S,W):
    SW[w].append(int(s))

SW=sorted(SW.items())
adult_cnt=[0]*(N+1)
child_cnt=[0]*N
for i in range(len(SW)):
    sw=SW[i]
    for s in sw[1]:
        if s==1:
            adult_cnt[i+1]+=1

        else:
            child_cnt[i]+=1
adult_sum=list(accumulate(adult_cnt))
child_sum=[0]+list(accumulate(child_cnt))
ans=0

for i in range(N+1):
    ans=max(ans,ad_max-adult_sum[i]+child_sum[i])

print(ans)


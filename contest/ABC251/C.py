N=int(input())

from collections import defaultdict
score=defaultdict(list)

for i in range(N):
    s,t=map(str,input().split())
    t=int(t)
    if s not in score:
        score[s]=[t,i+1]

ans=0
ans_number=0

for t,i in score.values():
    
    if ans<t:
        ans=t
        ans_number=i


print(ans_number)
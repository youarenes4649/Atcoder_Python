N=int(input())
from collections import defaultdict
import sys
lis=defaultdict(list)
for i in range(1,2*N+2):
    lis[i]=True#使えるのであればTrue

count=0
while count<N+1:
    count+=1
    for i in range(1,2*N+2):
        if lis[i]==True:
            print(i)
            sys.stdout.flush()
            lis[i]=False
            break

    
    aoki=int(input())
    if lis[aoki]==True:
        lis[aoki]=False

    
    




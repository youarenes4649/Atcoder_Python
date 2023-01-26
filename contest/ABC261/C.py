N=int(input())
from collections import defaultdict
count=defaultdict(int)
for i in range(N):
    s=input()
    if count[s]==0:
        print(s)
        

    else:
        print(s+'('+str(count[s])+')')

    count[s]+=1
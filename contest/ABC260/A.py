S=input()
from collections import defaultdict
count=defaultdict(int)
for s in S:
    count[s]+=1

for s in S:
    if count[s]==1:
        print(s)
        exit()
    
print(-1)


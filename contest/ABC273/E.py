Q=int(input())
from collections import defaultdict
page=defaultdict(int)
A=[]
ans=[]
for q in range(Q):
    query=list(input().split())
    if query[0]=='ADD':
        A.append(int(query[1]))
    elif query[0]=='SAVE':
        page[int(query[1])]=A[-1]
    elif query[0]=='DELETE':
        if len(A)==0:
            ans.append(-1)
            continue
        else:
            A.pop()
    else:
        A=[page[int(query[1])]]
        

    if len(A)==0:
        ans.append(-1)

    else:
        if A[-1]==0:
            ans.append(-1)
        else:
            ans.append(A[-1])

print(*ans)
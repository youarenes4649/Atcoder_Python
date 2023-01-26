Q=int(input())
from collections import deque
stack=deque()
answers=[]
for i in range(Q):
    ans=0
    query=list(map(str,input().split()))

    if query[0]=='1':
        x,c=int(query[1]),int(query[2])
        stack.append([x,c])

    else:
        c=int(query[1])
        while c>0:

            if stack[0][1]>=c:
                ans+=c*stack[0][0]
                stack[0][1]-=c
                c=0

            else:
            

                a,b=stack.popleft()
                ans+=a*b
                c-=b

        answers.append(ans)


for ans in answers:
    print(ans)





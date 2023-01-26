N=int(input())
A=list(map(int,input().split()))
from collections import defaultdict
from collections import deque
import bisect
count=defaultdict(int)
cnt=0
A.sort()
A_s=set(A)
A_de=deque(A)
ans=[]
for i in range(1,N+1):
    if A[i-1]==i:
        cnt+=1
        ans.append(i)
    count[A[i-1]]+=1
if cnt==0:
    print(0)
    exit()
c=cnt+1
while True:
    A_s=set(A_de)
    if c not in A_s:#もしなかったら
        idx = bisect.bisect_right(A_de,c)
        if idx-c==1:#1さつつかえるとき
            one=A_de.popleft()
            count[one]-=1
            if A_de[-1]>c:#もしcよりデカかったらok
                sec=A_de.pop()
                count[sec]-=1
                ans.append(c)
            else:
                print(ans[-1])
                exit()

        elif idx-c>1:#2札使う
            one=A_de.pop()
            sec=A_de.pop()
            count[one]-=1
            count[sec]-=1
            ans.append(c)
            print(1)
        
        else:#1未満つまりidxがあってるとき
            if A_de[-2]>c:#もしcよりデカかったらok
                one=A_de.pop()
                sec=A_de.pop()
                count[one]-=1
                count[sec]-=1
                ans.append(c)

            else:
                print(ans[-1])
                exit()


    else:
        ans.append(c)
    c+=1
    
print(N)


        

        












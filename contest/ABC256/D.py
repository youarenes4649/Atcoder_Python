N=int(input())
L_R=[]
for i in range(N):
    l,r=map(int,input().split())
    L_R.append([l,r])

L_R.sort()
ans=[]
for l,r in L_R:
    if len(ans)==0:
        ans.append([l,r])

    elif l<=ans[-1][1]:
        ans[-1][1]=max(ans[-1][1],r)

    else:
        ans.append([l,r])



for a in ans:
    print(*a)



    
    

    
    

N,K=map(int,input().split())
xy=[]
for i in range(N):
    x,y=map(int,input().split())
    xy.append((x,y))

ans=0
if K==1:
    print('Infinity')
    exit()

for i in range(N):
    x1,y1=xy[i]
    for j in range(i+1,N):
        x2,y2=xy[j]
        tmp=0
        flg=False
        for a in range(N):
            x3,y3=xy[a]

            if (x3-x1)*(y2-y1)==(x2-x1)*(y3-y1):
                if (a!=i and a!=j and a<j):
                    frg=True
                    break

                tmp+=1

        if flg:
            continue

        if tmp>=K:
            ans+=1

print(ans)





